from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("driver/chromedriver.exe")


driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.carulla.com/")
time.sleep(1)

#abre el menu
menu = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/div/button/div')
menu.click()
#search.send_keys(clave)
time.sleep(1)

#da click en vida sana
menuVida = driver.find_element(By.XPATH, '/html/body/div[12]/div[3]/div/div/div[1]/ul/li[6]')
menuVida.click()
time.sleep(1)

#da click en libre de gluten
menuGluten = driver.find_element(By.LINK_TEXT, 'Libre de gluten')
menuGluten.click()
time.sleep(5)

#pagina libre de gluten

#da click en menu para seleccionar una cuidad
pedidoMenu = driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]')
pedidoMenu.click()
time.sleep(1)

#da click en medellin
pedidoCuidad = driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/div/div[2]/div/div[3]')
pedidoCuidad.click()
time.sleep(1)

#da click en menu para seleccionar un almacen
pedidoMenu = driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[3]/div[2]/div/div/div')
pedidoMenu.click()
time.sleep(1)

#da click en el primer almacen
pedidoAlmacen = driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div/div[2]/div[4]/div[3]/div[2]/div/div[2]/div/div[1]')
pedidoAlmacen.click()
time.sleep(1)

#da click en aceptar
pedidoAceptar = driver.find_element(By.XPATH, '/html/body/div[9]/div[1]/div/div/div[2]/div[6]/button')
pedidoAceptar.click()
time.sleep(5)

#hace un pequeño scroll
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(2)

#da click en fitro de Cereales, Avena Y Granolas
filtro = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[15]/section/div[2]/div/div[3]/div/div[1]/div/div[1]/div/div/div[3]/div[2]/div/div/div[5]/div/div/input')
filtro.click()
time.sleep(5)

for i in range(1, 5):
    nombres = f"/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[{i}]/section/a/article/div[3]/div[2]/div/div/div/div[2]/div/span"
    precios = f"/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[{i}]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span"

    nombre = driver.find_element(By.XPATH, nombres).text
    precio = driver.find_element(By.XPATH, precios).text

    print("Nombre:", nombre)
    print("Precio:", precio)
    print("-----")

time.sleep(1)

#da click a un producto
clickProducto = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[1]/section/a/article/div[3]/div[1]/div/div/div/img')
clickProducto.click()
time.sleep(5)

#hace scroll hasta el final de la pagina
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#da click al enlace de youtube
clickYoutube = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div/div[2]/section/div/div[3]/div/div[2]/div/div[1]/div[2]/a[4]')
clickYoutube.click()
time.sleep(5)

driver.quit()