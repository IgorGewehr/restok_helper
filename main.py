from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from win10toast import ToastNotifier

# Constantes
WAIT_TIME = 15
REFRESH_WAIT_TIME = 30

# One-time initialization
toaster = ToastNotifier()


def verificar_item_loja(driver, item_name):
    """
    Verifica se o item desejado está presente na loja.
    """
    # Encontre todos os elementos com a classe "shop-item" usando o driver
    shop_items = driver.find_elements(By.CLASS_NAME, 'shop-item')

    # Verificar cada item para ver se é o item desejado
    for item in shop_items:
        item_name_element = item.find_element(By.CLASS_NAME, 'item-name').text
        if item_name_element == item_name:
            print(f"Item desejado encontrado na loja: {item_name_element}")
            toaster.show_toast("Notification!", "Item desejado encontrado!!", threaded=True,
                               icon_path=None, duration=5)


def main():
    try:
        # Configuração do driver do Edge para as lojas do Neopets
        driver_options = webdriver.EdgeOptions()
        driver_options.use_chromium = True

        # Crie três novos drivers para as lojas do Neopets
        driver_shop1 = webdriver.Edge(options=driver_options)
        driver_shop2 = webdriver.Edge(options=driver_options)
        driver_shop3 = webdriver.Edge(options=driver_options)

        # Acessar as páginas das lojas do Neopets
        driver_shop1.get('https://www.neopets.com/objects.phtml?type=shop&obj_type=103')
        driver_shop2.get('https://www.neopets.com/objects.phtml?type=shop&obj_type=61')
        driver_shop3.get('https://www.neopets.com/objects.phtml?type=shop&obj_type=97')

        time.sleep(WAIT_TIME)

        contador = 0

        while True:
            # Chamar a função para verificar o item em cada loja
            # Shenkuu
            verificar_item_loja(driver_shop1, "Pandaphant")
            # Neve
            verificar_item_loja(driver_shop2, "Candychan")
            # Altador
            verificar_item_loja(driver_shop3, "Minitheus")

            # Incrementar o contador a cada volta do loop
            contador += 1

            # Imprimir o valor do contador
            print(f"Número de voltas do loop: {contador}")

            # Aguardar o tempo antes de atualizar a página novamente
            time.sleep(REFRESH_WAIT_TIME)

            # Atualizar a página de cada loja
            driver_shop1.refresh()
            driver_shop2.refresh()
            driver_shop3.refresh()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
