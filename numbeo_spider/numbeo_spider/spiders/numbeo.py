import scrapy

class NumbeoSpider(scrapy.Spider):
    # identidade
    name = 'numbeo'
    # request
    def start_requests(self):
        # Definir as urls para varrer
        city = 'Helsinki'
        urls = [f'https://www.numbeo.com/cost-of-living/in/{city}']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    # Response
    def parse(self, response):
        # Aqui é onde processamos o que é retornado da response
        # laço for para pegar mais de um elemento
        # usamos o xpath da div que contém todos os elementos que queremos buscar
        for elemento in response.xpath('//table[@class="data_wide_table new_bar_table"]'): 
            yield{
                'name': elemento.xpath('//span[@class="purple_light"]//text()').get(),
                'common_meal': elemento.xpath('.//tr[2]//td//span/text()').get(), # xpath do texto 
                'meal_for_two': elemento.xpath('.//tr[3]//td//span/text()').get(), # xpath do texto 
                'one_way_ticket': elemento.xpath('.//tr[31]//td//span/text()').get(), # xpath do texto 
                'monthly_pass': elemento.xpath('.//tr[32]//td//span/text()').get(), # xpath do texto 
                'gasoline': elemento.xpath('.//tr[36]//td//span/text()').get(), # xpath do texto 
                'base_cost': elemento.xpath('.//tr[40]//td//span/text()').get(), # xpath do texto 
                'internet': elemento.xpath('.//tr[42]//td//span/text()').get(), # xpath do texto 
                'simple_apartment_centre': elemento.xpath('.//tr[56]//td//span/text()').get(), # xpath do texto 
                'simple_apartment_outside': elemento.xpath('.//tr[57]//td//span/text()').get(), # xpath do texto 
                'large_apartment_centre': elemento.xpath('.//tr[58]//td//span/text()').get(), # xpath do texto 
                'large_apartment_outside': elemento.xpath('.//tr[59]//td//span/text()').get(), # xpath do texto 
                'salary': elemento.xpath('.//tr[64]//td//span/text()').get(), # xpath do texto 
                'status': elemento.xpath('//div[@class="align_like_price_table"]//text()[2]').get(),
            } 