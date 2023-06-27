from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
import pytest
from time import sleep

class Test_VakıfBank:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.vakifbank.com.tr")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()
    
    def waitMethod(self,locator):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((locator)))

    def scrollMethod(self):
        self.driver.execute_script("window.scrollTo(0,500)")
    
    def nextMtehod(self):
         for i in range(1,11):
            btnNext = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[5]/div[2]/div/div/div/div/button[2]")
            sleep(2)
            btnNext.click()

    def test_investorRelations(self):
        actions = ActionChains(self.driver)
        self.waitMethod((By.XPATH,"//*[@id='Form1']/div[3]/div/div/div/div/div[2]/div/a[3]"))
        btnRelations = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[3]/div/div/div/div/div[2]/div/a[3]")
        btnRelations.click()
        self.driver.save_screenshot(f"{self.folderPath}/1.png")
        self.scrollMethod()

        #banka bilgilerimiz
        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl00_hypLink"))
        btnInformation = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl00_hypLink")
        btnInformation.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/2.png")
        self.driver.execute_script("window.scrollTo(0,0)")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl02_hypLink"))
        btnPartnership = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl02_hypLink")
        btnPartnership.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/3.png")
        self.driver.execute_script("window.scrollTo(0,0)")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl03_hypLink"))
        btnMembers = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl03_hypLink")
        btnMembers.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/4.png")
        self.driver.execute_script("window.scrollTo(0,0)")

        self.waitMethod((By.ID,"ctl00_ctl46_ctl00_rptMenu_ctl04_hypLink"))
        btnUpperMembers = self.driver.find_element(By.ID,"ctl00_ctl46_ctl00_rptMenu_ctl04_hypLink")
        btnUpperMembers.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/5.png")
        self.driver.execute_script("window.scrollTo(0,0)")

        #kurumsal Yönetim
        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl06_hypLink"))
        btnInstituonal = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl06_hypLink")
        btnInstituonal.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/6.png")
        self.driver.execute_script("window.scrollTo(0,0)")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl08_hypLink"))
        btnCompliance = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl08_hypLink")
        btnCompliance.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/7.png")
        self.driver.execute_script("window.scrollTo(0,0)")

        self.waitMethod((By.XPATH,"//a[@id='ctl00_ctl22_ctl00_rptMenu_ctl09_hypLink']/span"))
        btnDegree = self.driver.find_element(By.XPATH,"//a[@id='ctl00_ctl22_ctl00_rptMenu_ctl09_hypLink']/span")
        actions.move_to_element(btnDegree).perform()
        btnDegree.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/8.png")
        self.driver.execute_script("window.scrollTo(0,0)")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl10_hypLink"))
        btnComite = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl10_hypLink")
        btnComite.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/9.png")
        self.driver.execute_script("window.scrollTo(0,200)")

        self.waitMethod((By.ID,"ctl00_ctl18_ctl00_rptMenu_ctl11_hypLink"))
        btnClose = self.driver.find_element(By.ID,"ctl00_ctl18_ctl00_rptMenu_ctl11_hypLink")
        btnClose.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/10.png")
        self.driver.execute_script("window.scrollTo(0,300)")

        self.waitMethod((By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl12_hypLink']/span"))
        btnPolicy = self.driver.find_element(By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl12_hypLink']/span")
        btnPolicy.click()
        self.driver.save_screenshot(f"{self.folderPath}/11.png")
        self.scrollMethod()
        self.waitMethod((By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl14_hypLink']/span"))
        btnPolicy1 = self.driver.find_element(By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl14_hypLink']/span")
        btnPolicy1.click()
        self.driver.execute_script("window.scrollTo(0,1500)")
        self.driver.save_screenshot(f"{self.folderPath}/11-1.png")

        self.waitMethod((By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl35_hypLink']/span"))
        btnContract = self.driver.find_element(By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl35_hypLink']/span")
        btnContract.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/12.png")

        self.waitMethod((By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl36_hypLink']/span"))
        btnLaw = self.driver.find_element(By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl36_hypLink']/span")
        btnLaw.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/13.png")
        self.driver.execute_script("window.scrollTo(0,300)")

        self.waitMethod((By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl37_hypLink']/span"))
        btnExample = self.driver.find_element(By.XPATH,"//a[@id='ctl00_ctl16_ctl00_rptMenu_ctl37_hypLink']/span")
        btnExample.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/14.png")
        self.driver.execute_script("window.scrollTo(0,300)")

        #finansal bilgiler
        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl39_hypLink"))
        btnFinancial = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl39_hypLink")
        btnFinancial.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/15.png")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl41_hypLink"))
        btnReport = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl41_hypLink")
        btnReport.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/16.png")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl43_hypLink"))
        btnUfrs = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl43_hypLink")
        btnUfrs.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/17.png")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl44_hypLink"))
        btnActivity = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl44_hypLink")
        btnActivity.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/18.png")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl45_hypLink"))
        btnBddk = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl45_hypLink")
        btnBddk.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/19.png")

        #yatırımcı sunumları
        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl47_hypLink"))
        btnInvestor = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl47_hypLink")
        btnInvestor.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/20.png")

        #hisse senedi
        self.waitMethod((By.ID,"ctl00_ctl24_ctl00_rptMenu_ctl48_hypLink"))
        btnShare = self.driver.find_element(By.ID,"ctl00_ctl24_ctl00_rptMenu_ctl48_hypLink")
        btnShare.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/21.png")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl50_hypLink"))
        btnHistory = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl50_hypLink")
        btnHistory.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/22.png")

        self.waitMethod((By.ID,"ctl00_ctl18_ctl00_rptMenu_ctl51_hypLink"))
        btnGraphics = self.driver.find_element(By.ID,"ctl00_ctl18_ctl00_rptMenu_ctl51_hypLink")
        btnGraphics.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/23.png")

        self.waitMethod((By.ID,"ctl00_ctl18_ctl00_rptMenu_ctl52_hypLink"))
        btnShares = self.driver.find_element(By.ID,"ctl00_ctl18_ctl00_rptMenu_ctl52_hypLink")
        btnShares.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/24.png")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl53_hypLink"))
        btnRatio = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl53_hypLink")
        btnRatio.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/25.png")

        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl54_hypLink"))
        btnAnalist = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl54_hypLink")
        btnAnalist.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/26.png")

        #özeldurumaçıklamaları
        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl56_hypLink"))
        btnPrimary = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl56_hypLink")
        btnPrimary.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/27.png")

        #basın açıklamaları
        self.waitMethod((By.ID,"ctl00_ctl34_ctl00_rptMenu_ctl57_hypLink"))
        btnNews = self.driver.find_element(By.ID,"ctl00_ctl34_ctl00_rptMenu_ctl57_hypLink")
        btnNews.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/28.png")

        #sürdürülebilirlik
        self.waitMethod((By.ID,"ctl00_ctl14_ctl00_rptMenu_ctl58_hypLink"))
        btnCont = self.driver.find_element(By.ID,"ctl00_ctl14_ctl00_rptMenu_ctl58_hypLink")
        btnCont.click()
        self.driver.execute_script("window.scrollTo(0,900)")
        self.driver.save_screenshot(f"{self.folderPath}/29.png")

        #ratin bilgiler
        self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl90_hypLink"))
        btnRating = self.driver.find_element(By.ID,"ctl00_ctl16_ctl00_rptMenu_ctl90_hypLink")
        btnRating.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/30.png")

        #hesaplama araçları
        self.waitMethod((By.XPATH,"//*[@id='Form1']/div[5]/div[2]/div/div/div[1]/div[2]/a[1]"))
        btnCalc = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[5]/div[2]/div/div/div[1]/div[2]/a[1]")
        btnCalc.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/31.png")
        self.driver.execute_script("window.scrollTo(0,0)")

    #hakkımızda
    def test_about(self):
        self.waitMethod((By.XPATH,"//*[@id='Form1']/div[3]/div/div/div/div/div[2]/div/a[2]"))
        btnAbout = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[3]/div/div/div/div/div[2]/div/a[2]")
        btnAbout.click()
        self.driver.execute_script("window.scrollTo(0,200)")
        self.driver.save_screenshot(f"{self.folderPath}/32.png")
        self.driver.execute_script("window.scrollTo(0,700)")
        self.driver.save_screenshot(f"{self.folderPath}/33.png")
    
    #internet bankacılığı
    def test_bank(self):
        actions = ActionChains(self.driver)
        btnBank = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[3]/div/div/div/div/div[1]/div/div[2]")
        actions.move_to_element(btnBank).perform()
        self.driver.save_screenshot(f"{self.folderPath}/34.png")
    
    #üst butonlar
    def test_topBtn(self):
        #Bireysel
        self.waitMethod((By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl00_hypLink"))
        btnSingular = self.driver.find_element(By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl00_hypLink")
        btnSingular.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.save_screenshot(f"{self.folderPath}/35.png")
        self.nextMtehod()
        btnLink = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl16_ctl00_rptNews_ctl09_ctl00_lblDescription']/a")
        btnLink.click()
        self.driver.save_screenshot(f"{self.folderPath}/36.png")
        self.driver.back()
        self.scrollMethod()
        for i in range(4):
            self.waitMethod((By.ID,"ctl00_ctl18_ctl00_rptNews_ctl00_ctl00_hypNewsDetail3"))
            btnSecu = self.driver.find_element(By.ID,f"ctl00_ctl18_ctl00_rptNews_ctl0{i}_ctl00_hypNewsDetail3")
            btnSecu.click()
            self.driver.save_screenshot(f"{self.folderPath}/37-{i}.png")
            self.driver.back()
        self.scrollMethod()
        self.driver.back()

        #kobi
        self.waitMethod((By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl01_hypLink"))
        btnKobi = self.driver.find_element(By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl01_hypLink")
        btnKobi.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.save_screenshot(f"{self.folderPath}/38.png")
        self.nextMtehod()
        btnInf = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl16_ctl00_rptNews_ctl09_ctl00_lblDescription']/span/a")
        btnInf.click()
        self.scrollMethod()
        self.driver.save_screenshot(f"{self.folderPath}/39.png")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0,600)")
        for j in range(4):
            btnBott = self.driver.find_element(By.ID,f"ctl00_ctl18_ctl00_rptNews_ctl0{j}_ctl00_lblHeaderText")
            btnBott.click()
            self.driver.save_screenshot(f"{self.folderPath}/40-{j}.png")
            self.driver.back()
        self.driver.execute_script("window.scrollTo(0,1100)")
        self.driver.save_screenshot(f"{self.folderPath}/41.png")
        self.driver.back()

        #ticari
        self.waitMethod((By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl02_hypLink"))
        btnSeller = self.driver.find_element(By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl02_hypLink")
        btnSeller.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.save_screenshot(f"{self.folderPath}/42.png")
        self.nextMtehod()
        btnInfo = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl16_ctl00_rptNews_ctl01_ctl00_lblDescription']/span/a")
        btnInfo.click()
        self.driver.save_screenshot(f"{self.folderPath}/43.png")
        self.driver.execute_script("window.scrollTo(0,200)")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0,800)") 
        for k in range(4):
            btnBotto = self.driver.find_element(By.ID,f"ctl00_ctl18_ctl00_rptNews_ctl0{k}_ctl00_lblHeaderText")
            btnBotto.click()
            self.driver.execute_script("window.scrollTo(0,300)")
            self.driver.save_screenshot(f"{self.folderPath}/44-{k}.png")
            self.driver.back()
        self.driver.execute_script("window.scrollTo(0,1200)")
        self.driver.back()     

        #kurumsal
        self.waitMethod((By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl03_hypLink"))
        btnInstitutional = self.driver.find_element(By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl03_hypLink")
        btnInstitutional.click()
        self.driver.save_screenshot(f"{self.folderPath}/45.png")
        self.driver.execute_script("window.scrollTo(0,300)")  
        self.nextMtehod()
        self.waitMethod((By.XPATH,"//*[@id='ctl00_ctl16_ctl00_rptNews_ctl02_ctl00_lblDescription']/span/a"))
        btnAllSec = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl16_ctl00_rptNews_ctl02_ctl00_lblDescription']/span/a")
        btnAllSec.click()
        self.driver.execute_script("window.scrollTo(0,200)")
        self.driver.save_screenshot(f"{self.folderPath}/46.png")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0,800)")
        for l in range(4):
            btnBottom = self.driver.find_element(By.ID,f"ctl00_ctl18_ctl00_rptNews_ctl0{l}_ctl00_lblHeaderText")
            btnBottom.click()
            self.driver.save_screenshot(f"{self.folderPath}/47.png")
            self.driver.back()
        self.driver.execute_script("window.scrollTo(0,1200)")
        self.driver.back()

        #özel Bankacılı
        self.waitMethod((By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl04_hypLink"))
        btnPri = self.driver.find_element(By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl04_hypLink")
        btnPri.click()
        self.driver.save_screenshot(f"{self.folderPath}/48.png")
        self.driver.execute_script("window.scrollTo(0,300)")
        self.nextMtehod()
        self.waitMethod((By.XPATH,"//*[@id='ctl00_ctl16_ctl00_rptNews_ctl00_ctl00_lblDescription']/span/a"))
        btnInfor = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl16_ctl00_rptNews_ctl00_ctl00_lblDescription']/span/a")
        btnInfor.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.save_screenshot(f"{self.folderPath}/49.png")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0,700)")
        for m in range(4):
            btnPrim = self.driver.find_element(By.ID,f"ctl00_ctl18_ctl00_rptNews_ctl0{m}_ctl00_lblHeaderText")
            btnPrim.click()
            self.driver.execute_script("window.scrollTo(0,300)")
            self.driver.save_screenshot(f"{self.folderPath}/50-{m}.png")
            self.driver.back()
        self.driver.execute_script("window.scrollTo(0,1100)")
        self.driver.back()

        #yatırım
        self.waitMethod((By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl05_hypLink"))
        btnInvest = self.driver.find_element(By.ID,"ctl00_ctl06_ctl00_rptMenu_ctl05_hypLink")
        btnInvest.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.save_screenshot(f"{self.folderPath}/51.png")
        self.nextMtehod()
        btnInform = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl18_ctl00_rptNews_ctl02_ctl00_lblDescription']/span/a")
        btnInform.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.save_screenshot(f"{self.folderPath}/52.png")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0,800)")
        for n in range(4):
            btnCoin = self.driver.find_element(By.ID,f"ctl00_ctl20_ctl00_rptNews_ctl0{n}_ctl00_lblHeaderText")
            btnCoin.click()
            self.driver.execute_script("window.scrollTo(0,300)")
            self.driver.save_screenshot(f"{self.folderPath}/53-{n}.png")
            self.driver.back()
        self.driver.execute_script("window.scrollTo(0,1200)")
        self.driver.back()
        
    #ana slider
    def test_mainPage(self):
        self.driver.execute_script("window.scrollTo(0,200)")
        self.waitMethod((By.XPATH,"//*[@id='Form1']/div[5]"))
        for i in range(1,11):
            self.waitMethod((By.XPATH,"//*[@id='Form1']/div[5]/div/div/button[2]"))
            btnSlider = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[5]/div/div/button[2]")           
            btnSlider.click()
            sleep(1)
            self.driver.save_screenshot(f"{self.folderPath}/54-{i}.png")
        
        self.waitMethod((By.XPATH,"//*[@id='Form1']/div[5]/div/div/div/div/div[11]/div/div/div/div/a"))
        btnInfo = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[5]/div/div/div/div/div[11]/div/div/div/div/a")
        btnInfo.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        self.driver.save_screenshot(f"{self.folderPath}/55.png")
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0,400)")
        for j in range(1,6):
            btnCenter = self.driver.find_element(By.XPATH,f"//*[@id='Form1']/div[6]/div/div/div/div/div/div/a[{j}]") 
            btnCenter.click()
            self.driver.execute_script("window.scrollTo(0,800)")
            self.driver.save_screenshot(f"{self.folderPath}/56-{j}.png")
            sleep(2)
            self.driver.execute_script("window.scrollTo(0,400)")
        self.driver.execute_script("window.scrollTo(0,1200)")

        for k in range(6):
            self.waitMethod((By.ID,"ctl00_ctl16_ctl00_rptNews_ctl00_ctl00_hypNewsDetail3"))
            btnbott = self.driver.find_element(By.ID,f"ctl00_ctl16_ctl00_rptNews_ctl0{k}_ctl00_hypNewsDetail3")
            btnbott.click()
            self.driver.execute_script("window.scrollTo(0,300)")
            self.driver.save_screenshot(f"{self.folderPath}/57-{k}.png")
            self.driver.back()

        self.driver.execute_script("window.scrollTo(0,1500)")

        for l in range(16):
            self.waitMethod((By.XPATH,"//*[@id='Form1']/div[9]/div/div/div[2]/div/div/button[2]"))
            btnNext = self.driver.find_element(By.XPATH,"//*[@id='Form1']/div[9]/div/div/div[2]/div/div/button[2]")
            btnNext.click()
        self.driver.save_screenshot(f"{self.folderPath}/58.png")

        self.driver.execute_script("window.scrollTo(0,2100)")
        self.driver.save_screenshot(f"{self.folderPath}/59.png")