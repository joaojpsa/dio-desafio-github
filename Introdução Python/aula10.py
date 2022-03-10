#DATA HORA

from datetime import date, time, datetime

def trab_datetime():
    data_recente = datetime.now();
    print(data_recente);
    print(data_recente.strftime("%c"));
    print(data_recente.day); #hora, dia, ano, etc...
    
def trab_date():
    data_atual = date.today();
    print(data_atual);
    print(data_atual.strftime("%d/%m/%y"));
    print(data_atual.strftime("%d/%m/%Y"));
    print(data_atual.strftime("%d %m %Y"));
    print(data_atual.strftime("%A %B %Y"));

def trab_time():
    horario = time (hour=15, minute=30, second=10);
    print(horario.strftime("%H:%M:%S"));
    
if __name__ == "__main__":
    trab_date();
    trab_time();
    trab_datetime();