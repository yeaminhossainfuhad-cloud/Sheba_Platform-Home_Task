#Leave application without mandatory fields
import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_apply_leave_complete_flow():
    """Complete test flow for leave application"""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # Step 1: Login
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")))
        username_field.send_keys("Admin")

        password_field = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
        password_field.send_keys("admin123")

        login_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
        login_button.click()

        # Verify login
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6")))
        assert "Dashboard" in driver.page_source


        # Step 2: Navigate to Apply Leave
        leave_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a")))
        leave_menu.click()

        apply_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]")))
        apply_menu.click()

        # Verify navigation
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/h6")))


        # Add comment
        comment_field = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div[2]/textarea")
        comment_field.send_keys("Automated test leave application")

        # Submit
        apply_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button")
        apply_button.click()

        time.sleep(3)

        # Verify Show "Required"
        success_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/span")))

        assert success_element.is_displayed()
        print("Test passed")

    except Exception as e:
        driver.save_screenshot("test_failure.png")
        pytest.fail(f"Test failed: {str(e)}")

    finally:
        driver.quit()



