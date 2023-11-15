import pandas as pd
from googlesearch import search
from playwright.sync_api import sync_playwright

def get_linkedin_url(company_name):
    print(f"Searching for LinkedIn URL for {company_name}...")
    query = f"{company_name} LinkedIn"
    try:
        result = next(search(query, num_results=1, sleep_interval=2), None)
        if result and 'linkedin.com/company/' in result:
            print(f"LinkedIn URL found for {company_name}: {result}")
            return result
    except StopIteration:
        pass
    print(f"No LinkedIn URL found for {company_name}.")
    return None

def get_employee_count(linkedin_url):
    print(f"Getting employee count for {linkedin_url}...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(linkedin_url)

        page.wait_for_selector('xpath=/html/body/div[4]/div/div/section/button', timeout=5000)
        button_locator = page.locator('xpath=/html/body/div[4]/div/div/section/button')
        button_locator.click()

        page.wait_for_load_state('load')
        employee_count = 0

        page.wait_for_selector('xpath=/html/body/main/section[1]/section/div/div[2]/div[2]/ul/li/div/a', timeout=50000)
        employee_count_locator = page.locator('xpath=/html/body/main/section[1]/section/div/div[2]/div[2]/ul/li/div/a')

        if employee_count_locator:
            employee_count_sentence = employee_count_locator.text_content().strip()
            employee_count = int(''.join(filter(str.isdigit, employee_count_sentence)))
        else:
            page.wait_for_selector('xpath=/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/a/span', timeout=50000)
            employee_count_locator = page.locator('xpath=/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/a/span')
            if employee_count_locator:
                employee_count_sentence = employee_count_locator.text_content().strip()
                employee_count = int(''.join(filter(str.isdigit, employee_count_sentence)))

        browser.close()
        print(f"Employee count for {linkedin_url}: {employee_count}")
    return employee_count

def main(input_csv, output_csv):
    print("Starting the program...")
    
    # Read input CSV
    df_input = pd.read_csv(input_csv)

    # Create a new DataFrame for output
    df_output = pd.DataFrame(columns=['Company', 'LinkedIn URL', 'Employee Count'])

    for index, row in df_input.iterrows():
        company_name = row['Company']
        linkedin_url = get_linkedin_url(company_name)

        if linkedin_url:
            employee_count = get_employee_count(linkedin_url)
            df_output = pd.concat([df_output, pd.DataFrame([{'Company': company_name, 'LinkedIn URL': linkedin_url, 'Employee Count': employee_count}])], ignore_index=True)
        else:
            print(f"No LinkedIn URL found for {company_name}. Adding entry with missing data.")
            df_output = pd.concat([df_output, pd.DataFrame([{'Company': company_name, 'LinkedIn URL': None, 'Employee Count': None}])], ignore_index=True)

    # Write the output DataFrame to a new CSV file
    df_output.to_csv(output_csv, index=False)
    print(f"Program completed. Output saved to {output_csv}.")

if __name__ == "__main__":
    input_csv = 'input_companies.csv'
    output_csv = 'output_companies.csv'
    main(input_csv, output_csv)