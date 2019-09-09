from selenium import webdriver

class Sele:
    def __init__(self,anime_list):
        self.driver = None
        self.anime_list = anime_list
    
    def get_one_anime(self,anime_name):
        driver = webdriver.Chrome(executable_path='/Users/ken/Desktop/Python_code/chromedriver')
        driver.get('https://www.livechart.me/fall-2019/tv')
        element = driver.find_element_by_xpath('//*[@id="chart-search-query"]')
        element.send_keys(anime_name)
        self.anime_list = self.runner(driver)
        driver.close()
        return self.anime_list
    def get_all_anime(self):
        driver = webdriver.Chrome(executable_path='/Users/ken/Desktop/Python_code/chromedriver')
        driver.get('https://www.livechart.me/fall-2019/tv')
        self.anime_list = self.runner(driver)
        driver.close()
        return self.anime_list
    def runner(self,driver):
        temp = {}
        animes = driver.find_elements_by_class_name("anime-card")
        counter = 1
        if len(animes) > 0:
            for anime in animes:
                time = anime.find_element_by_xpath("""//*[@id="content"]/main/article[{}]/div/div[3]/div[1]""".format(counter))
                if time.text == '':
                    counter += 1
                    continue
                else:
                    title = anime.find_element_by_xpath("""//*[@id="content"]/main/article[{}]/div/h3""".format(counter))
                    counter += 1
                    if title.text not in temp:
                        temp[title.text] = time.text
                    else:
                        temp[title.text] = time.text
                    # print (title.text,':',time.text)
        else:
            print("no animes exist")
        return temp

if __name__=="__main__":
    pass
    # test = Sele()
    # test.get_one_anime("Dr")
    # test.get_all_anime()