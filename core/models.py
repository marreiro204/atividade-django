from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50)
    crm = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nome} - CRM: {self.crm} - especialidade {self.especialidade}"

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True,  null=True)
    data = models.DateTimeField()

    def __str__(self):
        return f"{self.paciente} atendido pelo médico: {self.medico}. data: {self.data}"    

