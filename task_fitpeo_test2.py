import time
import logging
from venv import logger
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_cordinates(element):
    location=element.location
    return location['x'],location['y']

def pixel_calculation(pixel_value,max_value,target_value):
    pc=(target_value*100)/max_value
    return pc

def test_fitpeo():
    #Initiating the Chrome driver
    driver = webdriver.Chrome()

    #Webdriver wait
    wait= WebDriverWait(driver,10)

    def check_box_elements(element):
        check_box_element=wait.until(EC.presence_of_element_located((By.XPATH,f"(//p[text()='{element}']/following::input[@type='checkbox'])[1]")))
        actions.move_to_element(check_box_element).perform()
        check_box_element.click()

    #Step-1 opening Fitpeo home page
    try:
        driver.get('https://www.fitpeo.com/')
        print("\nHome page opend sucessfully")
    except:
        print('unable to open home page')


    #Step-2: Clicking the Revenue Caluclator
    driver.find_element(By.XPATH,"//div[text()='Revenue Calculator']").click()
    print("Clicked Revenue caluculator")

    #waiting for 2 seconds to load the whole page completely
    time.sleep(3)

    #Step-3: Scrolling down till slider
    element= wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='CPT-99091']")))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform() 
    print("Scrolled till Slide Bar Successfully!")
    time.sleep(3)

    slider_point= wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(@class,'MuiSlider-thumb MuiSlider-thumbSizeMedium')]")))

    slider_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[@class='MuiSlider-root MuiSlider-colorPrimary MuiSlider-sizeMedium css-16i48op']//input[@type='range']")))


    #Step-4: Adjusting Slider
    input_value=wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(@class,'MuiInputBase-input')]")))
    max_value_of_slider =slider_element.get_attribute('max') #getting maximum value of slider
    Pixels=slider_point.get_attribute('style')
    default_pixel_value= Pixels.split("left: ")[1].split("%")[0] #extracting default pixel value

    #caluclating pixel value for 820
    desired_pixel_value=pixel_calculation(int(default_pixel_value),int(max_value_of_slider),820)

    #calucalting offset_x
    x=((abs(int(default_pixel_value)-desired_pixel_value)/100))*300 #300 is length of slider

    ActionChains(driver).drag_and_drop_by_offset(slider_element,x,0).perform()#slider adjustment
    time.sleep(3)
    assert int(input_value.get_attribute('value'))==820 
    print("Value updated to 820")

    #Step-5: Selecting CPT codes
    check_box_elements('CPT-99091')
    time.sleep(2)
    check_box_elements('CPT-99453')
    time.sleep(2)
    check_box_elements('CPT-99454')
    time.sleep(2)
    check_box_elements('CPT-99474')
    time.sleep(2)
    print("Checked all the boxes")


    #Step-9: 
    TRRP=wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='Total Recurring Reimbursement for all Patients Per Month:']")))
    TRRP.is_displayed()
    a=(TRRP.text).split(":")[-1].lstrip()
    assert a=='$110700' ,"Validated!"
    print("Validated Total Recurring Reimbursement for all Patients Per Month: $$110700. ")
    print("Sucessfully completed!")

    driver.quit()


