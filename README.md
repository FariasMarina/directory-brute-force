#[EN-PT/BR] Directory brute force 

[PT-BR]

## Sobre segurança ofensiva:
A segurança ofensiva se trata de invadir sistemas com intenção de melhorá-los, recordando tudo o que foi possível encontrar de vulnerabilidade potencial
ou existente para que posteriormente seja tratado com as medidas corretas.


## Força bruta em Cibersegurança:
Um ataque de força bruta busca violar senha, nome de usuários, URLs e chaves para criptografia. Tentar senha por senha, diretório por diretório e afins 
leva bastante tempo e trabalho, e por essa necessidade dos hackers surgiram os ataques de força bruta, como o nosso programa, que automatiza esse processo.

## Directory brute force:
Esta é uma ferramenta para automatizar a busca por subdomínios possivelmente vulneráveis, que podem conter informação sensível que não deveria ser mostrada,
como informações da LAN, páginas de login da administração (onde pode ocorrer mais tipos de ataque), versões de plugin, senhas de banco de dados e muitos outros.

<img>

## Como utilizar:

![alt text](images/example.png)




[ENGLISH]

Websites generally have subdomains that can contain sensitive information, such as databases passwords, plugins versions (that can contain exploits),
administrator login pages (that you shouldn't be allowed to access), LAN information and so on.

The thing is: finding all these subdomains manually is an exausting task. Directory brute-forces allow you to find these subdomains automatically.   

## But how do I know which subdomains insert on the website?

Subdomains can be found using wordlists. Wordlists are .txt files containing words in each line that can be passwords, subdomains, usernames
and everything that can be brute-forced. In this case, since we want to find hidden subdomains, we would use a subdomain wordlist.

You can read more about wordlists [here](https://www.sevenlayers.com/index.php/202-pentesting-101-passwords-and-wordlists).

## What is a directory brute force? 
A directory brute force is a tool to test different URLs from the same domain to find sensitive information weak security and try to
exploit them.


![alt text](images/example.png)
