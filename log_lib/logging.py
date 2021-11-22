class log:
    ##Обозначяем все основные локальные переменные
    def __init__(self, log_type="test", log_message="Test", write_file=True, debug_mode=True):
        import datetime
        from datetime import datetime
        self.type = log_type
        self.message = log_message
        self.write_file = write_file
        self.debug = debug_mode
        self.now = datetime.now()
        self.date_now = str(datetime.now())

    global write_to_file, test_var

    ##Тест определения переменных
    def test_var(self):
        print("___________________Значения переменных____________________________")
        print("Тип лога: ",self.type)
        print("Сообщение лога: ",self.message)
        print("Запись в файл: ",self.write_file)
        print("Режим debug: ",self.debug)
        print("Время: ",self.date_now)
        print("Максимальная длина сообщения лога: ", self.MAX_LEN)
        print("*******************Значения переменных*****************************")

    ##Сборка строки лога
    def build_log(self):
        ##Сборка log строки и даты + тип log
        self.log_only_data = "[{}] [{}]: ".format(self.date_now, self.type)
        self.log = "{}{}".format(self.log_only_data,self.message)

        ##Строка log
        print(self.log)


        self.MAX_LEN = 20   ##Максимальная длина сообщения лога
        self.len_log_only_data = int(len(self.log_only_data)) ##Длина только части с датой и log типом
        self.len_log_only_message = int(len(self.message))  ##Длина только сообщения лога
        self.len_log = int(len(self.log))   ##Длина всего log

        ##if self.len_log_only_message >= self.MAX_LEN:
            ##print("выфвыфв")

        ##Запись в файл при определённых условиях
        if self.write_file == True:
            write_to_file(self)

        ##Вывод дебаг информации при определённых условиях
        if self.debug == True:
            print("___________________Длина сообщений_______________________________")
            print("Длина лога без сообщения: ", self.len_log_only_data)
            print("Длина сообщения лога: ", self.len_log_only_message)
            print("Длина всего лога: ",self.len_log)
            print("*******************Длина сообщений********************************\n")
            test_var(self)

    ##Запись в файл
    def write_to_file(self):
        from pathlib import Path

        ##Запись в файл
        self.log_file = open("1.log", "a")
        self.log_file.write(self.log + "\n")
        self.log_file.close()

        ##Вывод дебаг информации при определённых условиях
        if self.debug == True:
            print("successfully")
            print("Путь файла ",Path(__file__).resolve().parent.parent)

##Если запускается сам файл библиотеки
if __name__ == "__main__":
    app = log("Error", "Okay")
    app.build_log()

