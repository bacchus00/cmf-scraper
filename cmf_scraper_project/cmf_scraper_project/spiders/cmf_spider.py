import scrapy
from ..items import CmfScraperProjectItem
from requests_html import HTMLSession

class CMFSpider(scrapy.Spider):
    root_url = True
    name = 'cmf'
    start_urls = [
        #https://www.cmfchile.cl/portal/principal/613/w3-propertyvalue-18591.html Emisores de Valores de Oferta Pública css('td') -> css('li') title="Registro de Directores, Admin. y Liq."
        'https://www.cmfchile.cl/institucional/mercados/entidad.php?mercado=V&rut=90690000&grupo=&tipoentidad=RVEMI&row=&vig=VI&control=svs&pestania=46'
    ]

    def parse(self, response):
        if root_url:
            companies_div = response.css('div#listado_fiscalizados').css('a::attr(href)')
        items = CmfScraperProjectItem()

        

        content = response.css('div#contenido')
        company_info = content.css('dd::text').extract()
        directors_table = content.css('tr')

        for element in directors_table:
            director_info = element.css('td::text').extract()
            if director_info:
                items['company_name'] = company_info[0]
                items['company_rut'] = company_info[1]
                items['director_rut'] = director_info[0]
                items['director_name'] = director_info[1]
                items['director_position'] = director_info[2]
                items['director_appointment_date'] = director_info[3]
                
                yield items
