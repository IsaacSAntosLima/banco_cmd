/* Banco_bancos: */

CREATE TABLE cliente (
    `id` PRIMARY KEY BIGINT NOT NULL AUTO_INCREMENT,
    `nome` VARCHAR(100) NOT NULL,
    `cpf` VARCHAR(11)
);

CREATE TABLE conta (
    `id` PRIMARY KEY BIGINT NOT NULL AUTO_INCREMENT,
    `saldo` DECIMAL(10,2) NOT NULL,
    `fk_cliente_id` BIGINT
);

CREATE TABLE transacao (
    `id` PRIMARY KEY BIGINT NOT NULL AUTO_INCREMENT,
    `tipo` ENUM('cartao','pix','ted'),
    valor DECIMAL(10,2) NOT NULL,
    `fk_conta_id` BIGINT
);
 
ALTER TABLE conta ADD CONSTRAINT FK_conta_2
    FOREIGN KEY (`fk_cliente_id`)
    REFERENCES cliente (`id`)
    ON DELETE CASCADE;
 
ALTER TABLE transacao ADD CONSTRAINT FK_transacao_2
    FOREIGN KEY (`fk_conta_id`)
    REFERENCES conta (`id`)
    ON DELETE CASCADE;