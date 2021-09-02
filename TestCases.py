from _ast import Assert
from typing import List
import driver as driver
import pytest
import switch as switch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Software_Shital/Selenium/Chrome_version_91/chromedriver.exe")
            driver.get("https://mystifying-beaver-ee03b5.netlify.app/")
            filter_data = driver.FindElement(By.XPath("//input[@id='filter-input']"))
            filter_data.SendKeys(filter)
            List sort1 = new List<string>[]
            List sort2 = new List<string>[]

            # Verify filter data in complexity.

        if filter==("low") || filter==("high") || filter==("medium"):
                val = driver.FindElements(By.XPath("//div[@class='table-data data-complexity']"))
                    for a in val:
                    Assert.IsTrue(a.Text.Contains(filter), "Complexity Column contains data other than " + filter)
                        else
                            val1 = driver.FindElements(By.XPath("//div[@class='table-data data-name']"))
                    for a in val1:
                        Assert.IsTrue(a.Text.ToLower().Contains(filter.ToLower()), "Name Column contains data other than " + filter)

    # Verify filter data in Name

    sortdrpdwn = driver.FindElement(By.XPath("//select[@id='sort-select']"))
    SelectElement SelectVal = new SelectElement(sortdrpdwn);
    SelectVal.SelectByText(sort)
    wait = WebDriverWait(driver, 10)

    # Verify sortdata based on the columns selected.

     switch Name:
            val2 = driver.FindElements(By.XPath("//div[@class='table-data data-name']"))
            for a in val2:
                    sort1.Add(a.Text)

    # sort2.Add(sort1.Sort())

    for string b in sort1 :
        sort2.Add(b)
        sort2.Sort()
    for i, j in range <sort1, range <sort2:
            Assert.IsTrue(sort1[i].Equals(sort2[j]), "values are equal"
    break;

    switch Number of cases:
    val2 = driver.FindElements(By.XPath("//div[@class='table-data data-cases']"))
    for a in val2:
        sort1.Add(a.Text)

    # sort2.Add(sort1.Sort())

    for string b in sort1:
                        sort2.Add(b)
                        sort2.Sort();
                    for i, j in range <sort1, range <sort2:
                        Assert.IsTrue(sort1[i].Equals(sort2[j]), "values are equal")
                    break
    switch Impact score:
    val2 = driver.FindElements(By.XPath("//div[@class='table-data data-averageImpact']"))
    for a in val2:
        sort1.Add(a.Text)
    break;

    switch Complexity:
    val2 = driver.FindElements(By.XPath("//div[@class='table-data data-complexity']"))
        for  a in val2:
    sort1.Add(a.Text)

    # sort2.Add(sort1.Sort())

    for string b in sort1:
        sort2.Add(b)
        sort2.Sort()
    for i, j in range <sort1, range <sort2:
        Assert.IsTrue(sort1[i].Equals(sort2[j]), "values are equal")
    break;


