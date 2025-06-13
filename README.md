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
-
![image](https://github.com/user-attachments/assets/207317d1-d60e-444e-9ba7-aca6c89972ae)
-
![image](https://github.com/user-attachments/assets/c6b5d510-eaa6-4ceb-b036-ed4dd4cc9e99)

---

## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: DJango, Visual Studio Code, GitHub, SQLite3<br>

## Uso 
Siga os passos abaixo para rodar o sistema localmente:

---

1- Acesse o terminal do seu computador. Com o Git instalado, clone o repositório
```bash
git clone https://github.com/Projetos-de-Extensao/PBE_ADS_25.1_8001_ALPHA.git
```

2- Abrir a pasta com o Visual Studio Code<br>

3- Abrir o terminal no VSCode e instalar as dependências do repositório
```bash
pip install -r requirements.txt
```

4- Acessar as pastas para iniciar a aplicação
```bash
cd src/alpha
```

5- Criar um super usuário para acessar o painel administrativo do formulário
```bash
python manage.py createsuperuser
```
Preencha as informações pessoais solicitadas corretamente e prossiga.

6- Iniciar o servidor do Django
```bash
python manage.py runserver
```

7- Acesse a aplicação<br><br>
Depois de iniciar a aplicação, digite o link fornecido no terminal abaixo: ![image](https://github.com/user-attachments/assets/b21b9f25-2099-4547-be74-7cdf66a68abc)<br><br>
Entre com seu usuário de admin criado, após isso, a aplicação já está funcionando localmente na sua máquina, caso tenha acontecido algum erro, revise os passos e tente novamente.<br><br>
Segue abaixo um vídeo do funcionamento do projeto.

---

## Vídeo
[Vídeo de Funcionamento do Projeto](https://www.youtube.com/watch?v=nOv-7iZqYm8)
