# ALPHA

**Número do Grupo**: 01<br>
**Código da Disciplina**: FGA0208-T01<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 202408380501  |  Enrique Labre |
| 202407278752  |  Pedro de Castro Kurtz |
| 202401590118  |  Jeronimo Chiclana |
| 202401000434  |  Julia Siodaro |

## Sobre 
Plataforma para gerenciamento e armazenamento de dados sobre o questionário do Censo 2022 com foco na Ilha Primeira.

## Screenshots
![image](https://github.com/user-attachments/assets/8ed5035f-bf0d-4510-a4ad-f903b769e719)
![image](https://github.com/user-attachments/assets/207317d1-d60e-444e-9ba7-aca6c89972ae)
![image](https://github.com/user-attachments/assets/c6b5d510-eaa6-4ceb-b036-ed4dd4cc9e99)


## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: DJango<br>
Descreva os pré-requisitos para rodar o seu projeto e os comandos necessários.
Insira um manual ou um script para auxiliar ainda mais.

## Uso 
Siga os passos abaixo para rodar o sistema localmente:

---

1- Clonar o repositório
```bash
git clone https://github.com/Projetos-de-Extensao/PBE_ADS_25.1_8001_ALPHA.git
```

2- Instalar as dependências do repositório
```bash
pip install -r requirements.txt
```

3- Acessar as pastas para iniciar a aplicação
```bash
cd src/alpha
```

4- Criar super usuário para acessar painel de Administrativo do formulário
```bash
python manage.py createsuperuser
```
Preencha as informações pessoais solicitadas corretamente

5- Iniciar o servidor do Django
```bash
python manage.py runserver
```

6- Acesse a aplicação
Acesse o [link](http://127.0.0.1:8000/admin/)

---

## Vídeo
[Vídeo de Funcionamento do Projeto](https://www.youtube.com/watch?v=nOv-7iZqYm8)

## Outros 
[Pesquisa sobre o Censo Demográfico do IBGE 2022](https://github.com/Projetos-de-Extensao/PBE_ADS_25.1_8001_ALPHA/blob/main/pesquisa%20censo%20demografico.md)<br>
[Brainstorm](https://github.com/Projetos-de-Extensao/PBE_ADS_25.1_8001_ALPHA/blob/main/docs/base/Brainstorm.md)<br>
[5W2H](https://github.com/Projetos-de-Extensao/PBE_ADS_25.1_8001_ALPHA/blob/main/docs/base/5w2h.md)
