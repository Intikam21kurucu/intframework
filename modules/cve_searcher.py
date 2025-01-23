#!/usr/bin/env python3
import requests
import json
import click
import re
#author:arunkumarv
#https://www.linkedin.com/in/arunkumarvenugopal/
click.echo(click.style('*' * 120, fg='cyan'))
click.echo(click.style('                                                 CVE Finder                                       ', fg='red', bold=True))
click.echo(click.style('search tool to use the NIST NVD ( National Vulnerability Database ) to fetch CVEs associated with a product @arun kumar v', fg='green'))
click.echo(click.style('*' * 120, fg='cyan'))

def print_cve_details(vulnerabilities):
    for vuln in vulnerabilities:
        cve_id = vuln['cve']['id']
        description = vuln['cve']['descriptions'][0]['value']
        print(f"{cve_id}: {description}")
        cve_link = f"https://nvd.nist.gov/vuln/detail/{cve_id}"
        click.echo(click.style(cve_link, fg='blue', underline=True))

def search_by_keyword(keyword):
    base_url =f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}"
    response = requests.get(base_url)
    response.raise_for_status()
    data = response.json()

    # Extract the CVE IDs and descriptions
    vulnerabilities = data['vulnerabilities']
    print_cve_details(vulnerabilities)
    return vulnerabilities

def search_by_cpe(cpe_name):
    base_url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={cpe_name}"
    response = requests.get(base_url)
    print(base_url)
    response.raise_for_status()
    data = response.json()

    # Extract the CVE IDs and descriptions
    vulnerabilities = data['vulnerabilities']
    print_cve_details(vulnerabilities)
    return vulnerabilities


def search_by_cve_id(cve_id):
    cve_id = cve_id.upper()
    base_url =f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"
    response = requests.get(base_url)
    response.raise_for_status()
    data = response.json()

    # Extract the CVE IDs and descriptions
    vulnerabilities = data['vulnerabilities']
    print_cve_details(vulnerabilities)
    return vulnerabilities

def search_by_prod(prod):
    input_string=prod
    url = f"https://services.nvd.nist.gov/rest/json/cpes/2.0?keywordSearch={input_string}"
    response = requests.get(url)
    # Check if the API returned a valid response
    if response.ok:
        response_json = response.json()
        if "resultsPerPage" in response_json and "products" in response_json:
            # Look for all occurrences of the input string in the response
            cpe_matches = []
            for product in response_json["products"]:
                cpe_match = re.search(r'cpe:2\.3:.*?:.*?:'+input_string, product["cpe"]["cpeName"])
                if cpe_match:
                    cpe_matches.append(cpe_match.group(0))
            if cpe_matches:
                # Print all unique matching CPEs with numbered responses
                unique_cpes = list(set(cpe_matches))
                for i, cpe in enumerate(unique_cpes, start=1):
                    print(f"{i}: {cpe}")

                # Ask the user to supply the number
                while True:
                    selected_num = input("Select the serial number tagged to CPE : ")
                    if not selected_num.isdigit():
                        print("Invalid input. Please enter a number.")
                        continue
                    selected_num = int(selected_num)
                    if selected_num < 1 or selected_num > len(unique_cpes):
                        print(f"Invalid number. Please enter a number between 1 and {len(unique_cpes)}.")
                        continue
                    break

                # Print the corresponding CPE
                selected_cpe = unique_cpes[selected_num - 1]
                print(f"You have selected CPE: {selected_cpe}")
                selected_cpe = unique_cpes[selected_num - 1]
                version = input('Enter the product version:')
                while not version:
                    version = input('Now please enter a valid product version:')
                cpe_s = f"{selected_cpe}:{version}"  
                print(f"You have selected:{cpe_s}")
                search_by_cpe(cpe_s)
            else:
                print(f"'{input_string}' not found in any CPEs")
        else:
            print("Invalid response from the NVD API")
    else:
        print(f"Error: {response.status_code} - {response.reason}")


def search_by_ver(cpe_name, version_start=None, version_end=None):
    base_url =f"https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString={cpe_name}"
    if version_start:
        base_url +=f"&versionStart={version_start}&versionStartType=including"
    if version_end:
        base_url +=f"&versionEnd={version_end}&versionEndType=excluding"
    response = requests.get(base_url)
    response.raise_for_status()
    data = response.json()

    # Extract the CVE IDs and descriptions

    vulnerabilities = data['vulnerabilities']
    print_cve_details(vulnerabilities)
    return vulnerabilities

# Prompt the user to select the search option
def search():
    while True:
        click.echo('Select the option:')
        click.echo('1. General keyword search')
        click.echo('2. Search using product name when CPE info is not known')
        click.echo('3. Search for CVEs of against specific CPE - type, vendor name, product, and version')
        click.echo('4. Search info for a CVE-ID')
        click.echo('5. Search for all CVEs affiliated with versions x.x through x.x of a specific CPE')
        click.echo('6. HELP')
        option = input('int4 cve_finder[Please choose option 1/2/3/4/5/6 or 0 to exit] >')

        if option == '1':
            keyword = input('Enter the keyword to search: ')
            print(f"CVEs for '{keyword}':")
            cves = search_by_keyword(keyword)
        elif option == '2':
            keyword = input("Enter the product name to search for: ")
            cves = search_by_prod(keyword)
        elif option == '3':
            click.echo("""NOTE: use 'a' for application | 'o' for operating system | 'h' for hardware | 'p' for others""")
            cpe_type = input('Enter the CPE type (a/o/h/p): ')
            while cpe_type not in ['a', 'o', 'h', 'p']:
                  cpe_type = input('Please enter a valid CPE type (a/o/h/p): ')
            vendor_name = input('Enter the vendor name: ')
            while not vendor_name:
                  vendor_name = input('Please enter a valid vendor name: ')
            product_name = input('Enter the product name: ')
            while not product_name:
                  product_name = input('Please enter a valid product name: ')
            version = input('Enter the product version: ')
            while not version:
                    version = input('Please enter a valid product version: ')
            cpe_name = f"cpe:2.3:{cpe_type}:{vendor_name}:{product_name}:{version}"
             # Fetch the CVEs
            print(f"CVEs for {cpe_name}:")
            cves = search_by_cpe(cpe_name)
        elif option == '4':
            cve_id = input('Enter the CVE-ID to search: ')
            print(f"CVE details for {cve_id}:")
            cves = search_by_cve_id(cve_id)
        elif option == '5':

            click.echo("""Enter CPE details NOTE: use 'a' for application | 'o' for operating system | 'h' for hardware | 'p' for others""")
            cpe_type = input('Enter the CPE type (a/o/h/p): ')
            while cpe_type not in ['a', 'o', 'h', 'p']:
                  cpe_type = input('Please enter a valid CPE type (a/o/h/p): ')
            vendor_name = input('Enter the vendor name: ')
            while not vendor_name:
                  vendor_name = input('Please enter a valid vendor name: ')
            product_name = input('Enter the product name: ')  
            while not product_name:
                  product_name = input('Please enter a valid product name: ')  
            cpe_name = f"cpe:2.3:{cpe_type}:{vendor_name}:{product_name}"

            version_start =input('Enter the starting version where start version included (optional): ')
            version_end =input('Enter the ending version where end version excluded (optional):')
            print(f"CVEs for '{cpe_name}' from versions {version_start} through {version_end}:")
            cves = search_by_ver(cpe_name, version_start, version_end)
        elif option == '6':
            help_descriptions={
            "1":"Find CVEs matching keyword search",
            "2":"Search using product name when CPE info is not known",
            "3":"Search for CVEs against specific CPE",
            "4":"Get details for a CVE-ID",
            "5":"Search for CVEs for specific CPE versions",
            "0":"Program EXIT"
            }
            for option, description in help_descriptions.items():
              click.echo(click.style(f"OPTION {option}:",fg='cyan'))
              click.echo(click.style(f"{description}",fg='blue'))

        elif option == '0':
            # Exit program
            print("Thank you for using NVD lookup tool....Exiting program...skadoooosh!!!...")
            break
        else:
            print("Invalid option. Please try again.")

search()