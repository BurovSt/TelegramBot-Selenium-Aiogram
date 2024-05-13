import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

bot = Bot(token="YOUR TOKEN")
dp = Dispatcher()

URL = "YOUR SITE"
CHROMEDRIVER_PATH = "C:\\chromedriver\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--headless")


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("YOUR START MESSAGE")


@dp.message()
async def message_handle(text):
    await text.answer("YOUR MESSAGE IF NEEDED")
    # Using ChromeDriver
    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    # Find element if string and enter text to it (search zone)
    input_element = driver.find_element(By.NAME, "NAME OF ELEMENT")
    input_element.send_keys(text.text.upper())
    await asyncio.sleep(1)

    # FIND BUTTON TO SEARCH AND CLICK IT
    check_button = driver.find_element(By.CLASS_NAME, "submit_btn_green")
    check_button.click()
    await text.answer("Получил информацию")
    await asyncio.sleep(1)

    # ANSWER TO REQUEST

    # NEGATIVE

    result_element = driver.find_element(By.XPATH, "ENTER X PATH")
    value = result_element.text
    await text.answer(value)

    try:
        # POSITIVE
        result_element = driver.find_element(By.XPATH, "ENTER X PATH")
        value = result_element.text
        await text.answer(value.upper())
        result_element = driver.find_element(By.XPATH, "ENTER X PATH")
        value = result_element.text
        await text.answer(value.upper())
        result_element = driver.find_element(By.XPATH, "ENTER X PATH")
        value = result_element.text
        await text.answer(value)
    except NoSuchElementException:
        pass

    # CLOSING BROWSER
    driver.quit()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
