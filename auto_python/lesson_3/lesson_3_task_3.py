from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "15", "7")

mail = Mailing(to_address, from_address, 500, "ABCDE12345")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")
