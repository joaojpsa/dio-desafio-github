class Televisao:
    def __init__(self):
        self.ligada = False;
        self.canal = 2;
    
    def power(self):
        if self.ligada:
            self.ligada = False;
        else:
            self.ligada = True;
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1;
    def diminui_ccanal(self):
        if self.ligada:
            self.canal -= 1;

televisao = Televisao();
print(televisao.ligada);
televisao.power();
print(televisao.ligada);
televisao.power();
print(televisao.ligada);
televisao.power();
print("--------------");

print(televisao.canal);
televisao.aumenta_canal();
televisao.aumenta_canal();
print(televisao.canal);
televisao.diminui_ccanal();
print(televisao.canal);
