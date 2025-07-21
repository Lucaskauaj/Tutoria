API RESTful com Segurança JWT

Essa aplicação é uma API RESTful feita em **Python/Flask** que implementa um sistema de autenticação e autorização baseado em **JSON Web Tokens (JWT)**. O objetivo é proteger os recursos da API garantindo que apenas usuários autenticados e autorizados acessem determinadas rotas.

---

## O que a aplicação faz

* **Cadastro de usuários:** permite criar novos usuários com perfil padrão `USER`.
* **Login:** valida email e senha e retorna dois tokens JWT:

  * **Access Token:** token de curta duração (ex: 30 minutos) para autenticar requisições.
  * **Refresh Token:** token de longa duração (ex: 7 dias) para renovar o Access Token sem precisar logar de novo.
* **Renovação de token:** permite obter um novo Access Token a partir do Refresh Token válido.
* **Proteção de rotas:** exige que rotas sensíveis só sejam acessadas com um Access Token válido.
* **Controle de acesso por perfil:**

  * Usuários com perfil `ADMIN` têm acesso completo a todos os recursos.
  * Usuários com perfil `USER` têm acesso restrito aos seus próprios dados e ações.
* **Armazenamento seguro:** o Refresh Token é armazenado no banco de dados para controle e possível revogação.

---

## Funcionalidades principais

* Endpoints públicos:

  * `POST /usuarios` — criar usuário.
  * `POST /auth/login` — autenticar e receber tokens.
  * `POST /auth/refresh` — renovar Access Token com Refresh Token.
  * `GET /mensagens` — listar mensagens (sem autenticação).

* Endpoints protegidos (requer token válido):

  * CRUD completo para usuários (com restrições por perfil).
  * Operações CRUD para mensagens e comentários com regras específicas de autorização.

---

## Tecnologias usadas

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* PyJWT
* bcrypt (para hash de senhas)
* SQLite (banco de dados, pode ser trocado)

---

## Segurança

* Senhas são armazenadas com hash bcrypt.
* Tokens JWT possuem expiração para evitar uso indevido.
* Refresh Tokens são guardados no banco e validados.
* Controle de acesso baseado no campo `role` do usuário.
