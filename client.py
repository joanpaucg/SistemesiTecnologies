#!/usr/bin/env/python
# -*- coding: utf-8 -*-
#''''
#CLient web per www.udl.cat
#@author:jpcg
#''''
import urllib2
from bs4 import BeautifulSoup
#classe que deriva de object
class Client(object):

    def get_web(self,page):
        """baixar-se la web"""
        f=urllib2.urlopen(page)
        html=f.read()
        f.close()
        return html
    #TODO:buscar el text
    def search_text(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        elements=soup.find_all("div","featured-links-item")
        resultats=[]
        for element in elements:
            data=element.find("time")["datetime"]
            title=element.find("span", "flink-title")
            if title:
                title=title.text
            else:
                title="Sense Titol"
            resultats.append((data,title))

        return resultats

        

    def main(self):
        web = self.get_web("http://www.udl.cat/")

        resultat=self.search_text(web)

        #FIXME:imprimir els resultats
        print (resultat)


if __name__ == "__main__":#name variable interna
    client = Client()
    client.main()
    pass
