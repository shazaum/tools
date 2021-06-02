-- Cria uma função/grupo/cargo...
CREATE ROLE readaccess;

-- Conceder acesso nas tabelas existentes
GRANT USAGE ON SCHEMA public TO readaccess;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readaccess;

-- Conceder acesso nas tabelas futuras
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readaccess;

-- Criar um usuário final com senha
CREATE USER nome-dousuario WITH PASSWORD 'senha';
GRANT readaccess TO nome-do-usuario;


-- Depois de criar a ROLE readaccess, eh soh adicionar os usuarios que voce queira dar acesso somente leitura a eles
-- com o comando grant readaccess to nome-do-usuario;
