import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By

import dateparser


JOB = input("Job offer to search : \n").replace(' ', '+').lower()
RESULTS_PER_PAGE = 30

class WScrapSpider(scrapy.Spider):
    
    name = 'w_scrap'
    url = f"https://www.welcometothejungle.com/fr/jobs?page=1&groupBy=job&sortBy=mostRelevant&aroundQuery=France%2C+France&refinementList%5Boffice.country_code%5D%5B%5D=FR&query={JOB}"
    
    def start_requests(self):
        
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        
        #setting up Chrome
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        desired_capabilities = options.to_capabilities()
        
        #downloading the page with selenium
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
        driver.get(url=self.url)
        
        #calculate the number of pages 
        result_number = int(Selector(text=driver.page_source).xpath("//div[@class='sc-dSfdvi jwenEF']/span/text()").get())
        number_of_page = result_number // RESULTS_PER_PAGE

        for _ in range(number_of_page):
        
            #converting selenium download into usable scrapy source code 
            cleaned_response = Selector(text=driver.page_source)

            #list of the offers
            results = cleaned_response.xpath("//ol[@data-testid='jobs_index-search-results']/li")

            for result in results:
                
                company = result.xpath(".//h4/text()").get()
                job = result.xpath(".//span[@class='ais-Highlight sc-1s0dgt4-13 AiZQk']/em/text()").getall()
                contract_type = result.xpath(".//span[@class='sc-1lvyirq-2 gRznTA']/span/text()").get()
                location = result.xpath(".//span[@class='sc-1lvyirq-2 gTmGWh']/text()").get()
                
                #getting the age of the offer and converting it in a readable date
                age = result.xpath(".//span[@class='sc-1lvyirq-2 gRznTA']/time/span/text()").get()
                date = dateparser.parse(age)
                
                #sending back all results
                yield {
                            'company' : company,
                            'job' : " ".join(job),
                            'contract_type' : contract_type,
                            'location' : location,
                            'date' : date.strftime('%m/%d/%Y')                       
                        }
            #click on the next button
            next_button = driver.find_element(By.XPATH, "//a[@aria-label='Next page']").click()

