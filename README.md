# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# AgroGreen Insight

## Grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/renatoruizcai">Renato Ruiz Cai</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b">Sabrina Otoni</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato">André Godoi Chiovato</a>


## 📜 Descrição

*O agronegócio brasileiro possui papel fundamental na economia nacional, sendo responsável por grande parte da produção de alimentos e geração de riqueza. No entanto, mesmo com avanços tecnológicos e mecanização, ainda existem desafios relevantes relacionados à **gestão eficiente de insumos agrícolas**, especialmente fertilizantes.*

*Em muitos cenários, produtores realizam aplicações de fertilizantes de forma recorrente, sem uma análise estruturada do retorno produtivo. Essa prática pode gerar consequências como aumento de custos operacionais, desgaste do solo e impactos ambientais que comprometem a sustentabilidade da produção no longo prazo.*

*Além disso, a ausência de histórico organizado e análise de dados dificulta a tomada de decisão baseada em evidências, fazendo com que o manejo agrícola dependa, em grande parte, da experiência empírica.*

*Diante desse contexto, surge a necessidade de soluções que auxiliem o produtor na **interpretação dos dados produtivos**, promovendo uma gestão mais eficiente e orientada à sustentabilidade.*


## 💡 Proposta da Solução

*O projeto **AgroGreen Insight** foi desenvolvido com o objetivo de apoiar a tomada de decisão no campo por meio da análise integrada de dados relacionados à aplicação de fertilizantes e à produção agrícola por talhão.*

*A solução permite registrar e organizar essas informações, transformando dados operacionais em indicadores que representam o desempenho produtivo e o nível de impacto ambiental. A partir dessa análise, o sistema gera automaticamente uma **avaliação do talhão** e uma **recomendação sustentável**, orientando o usuário na definição de estratégias mais equilibradas.*


## 🌍 Sustentabilidade no Agronegócio

*A abordagem adotada pelo sistema considera não apenas o resultado produtivo, mas também o impacto gerado pelas práticas agrícolas. Ao incluir o conceito de **risco ambiental** na análise, o projeto propõe uma visão mais completa da atividade agrícola.*

*A solução atua como um apoio à tomada de decisão, contribuindo para evitar o uso excessivo de fertilizantes que, quando aplicado de forma inadequada, pode levar à degradação do solo e à redução da qualidade ambiental ao longo do tempo.*

*Com isso, o sistema incentiva práticas mais conscientes, como o uso equilibrado de insumos e a busca por maior harmonia entre produtividade e preservação dos recursos naturais, contribuindo para um modelo de agricultura mais responsável e sustentável.*


## 🚀 Relevância da Solução

*O AgroGreen Insight contribui para o desenvolvimento do agronegócio ao transformar dados simples em informações estratégicas, permitindo que o produtor compreenda melhor o desempenho de suas operações.*

*Entre os principais benefícios da solução, destacam-se:*

- *apoio à tomada de decisão com base em dados;*
- *identificação de cenários de baixa eficiência produtiva;*
- *direcionamento para práticas mais sustentáveis;*
- *facilidade de uso, mesmo para usuários sem conhecimento técnico aprofundado.*

*Dessa forma, o sistema se apresenta como uma ferramenta acessível e aplicável no contexto real do campo, com potencial de evolução para cenários mais complexos.*


## 🔬 Evolução da Solução

*Este projeto representa um **protótipo de uma solução** que pode ser significativamente ampliada com a inclusão de dados mais robustos e específicos.*

*A incorporação de informações adicionais, como análise de solo, características detalhadas de cada cultura, variáveis climáticas e dados históricos mais completos, permitiria uma análise muito mais aprofundada e contextualizada.*

*Com essa evolução, o sistema poderia oferecer recomendações mais precisas e confiáveis, adaptadas às particularidades de cada ambiente produtivo, contribuindo de forma mais efetiva para a eficiência operacional, a sustentabilidade e a preservação ambiental.*

*Essa perspectiva reforça o potencial da solução como base para o desenvolvimento de ferramentas mais avançadas voltadas ao futuro do agronegócio.*


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>src</b>: Contém todo o código fonte da aplicação em Python, organizado de forma modular e orientada à separação de responsabilidades.

  - <code>main.py</code>: ponto de entrada da aplicação. Responsável por inicializar o banco de dados Oracle, sincronizar os dados do JSON e iniciar o sistema via menu interativo.

  - <code>menu.py</code>: responsável pela exibição e controle do menu no terminal, permitindo a navegação entre as funcionalidades do sistema.

  - <b>models</b>: contém as classes que representam as entidades do sistema.
    - <code>field.py</code>: representa um talhão agrícola, com atributos como nome, área e cultura.
    - <code>fertilizer_application.py</code>: representa uma aplicação de fertilizante vinculada a um talhão.
    - <code>production_record.py</code>: representa um registro de produção agrícola associado a um talhão.

  - <b>services</b>: camada responsável pela lógica de negócio da aplicação.
    - <code>register_service.py</code>: gerencia o cadastro, listagem e exclusão de talhões, aplicações de fertilizante e registros de produção.
    - <code>analysis_service.py</code>: realiza a análise de eficiência produtiva e classificação do risco ambiental com base nos dados registrados.
    - <code>recommendation_service.py</code>: gera recomendações sustentáveis a partir da análise dos dados, considerando uso de insumos, eficiência e impacto ambiental.

  - <b>data</b>: responsável pela persistência e manipulação dos dados.
    - <code>fields.json</code>: armazena os talhões cadastrados no sistema.
    - <code>fertilizer_applications.json</code>: armazena as aplicações de fertilizante registradas.
    - <code>production_records.json</code>: armazena os registros de produção agrícola.
    - <code>system_log.txt</code>: registra eventos importantes do sistema, como cadastros, exclusões e análises realizadas.
    - <code>json_manager.py</code>: realiza leitura e escrita dos dados em arquivos JSON.
    - <code>txt_manager.py</code>: responsável pela geração e registro de logs em arquivo texto.
    - <code>oracle_manager.py</code>: gerencia a conexão com o banco de dados Oracle, incluindo criação de tabelas, inserção, exclusão e sincronização dos dados.

  - <b>utils</b>: contém funções auxiliares reutilizáveis em diferentes partes do sistema.
    - <code>validators.py</code>: valida os dados de entrada do usuário, garantindo consistência e evitando erros de digitação.
    - <code>helpers.py</code>: contém funções auxiliares, como geração de IDs incrementais.
    - <code>formatters.py</code>: padroniza a exibição das informações no terminal, melhorando a legibilidade e usabilidade da aplicação.

- <b>README.md</b>: arquivo que apresenta uma visão geral do projeto, incluindo sua finalidade, estrutura, funcionamento e instruções de uso.


## 🧠 Regras de Negócio / Lógicas de Decisão

*O **AgroGreen Insight** foi desenvolvido para apoiar a tomada de decisão a partir de regras simples, objetivas e consistentes com o propósito do projeto: analisar o uso de insumos agrícolas sob a perspectiva de **eficiência produtiva** e **sustentabilidade ambiental**.*

*A lógica do sistema foi construída com base em três pilares principais:*

- *volume total de fertilizante aplicado em cada talhão;*
- *produção total registrada para esse talhão;*
- *relação entre insumo utilizado e resultado produtivo obtido.*


### 1. Classificação do uso de fertilizante

*O sistema calcula o **volume total de fertilizante** aplicado em cada talhão, somando todas as aplicações registradas.*

*A partir desse total, o uso é classificado em três níveis:*

- ***baixo**: até 50*
- ***moderado**: maior que 50 e até 100*
- ***alto**: acima de 100*


*Essa classificação permite identificar se o talhão apresenta um consumo reduzido, intermediário ou elevado de insumos.*


### 2. Classificação da eficiência produtiva

*A eficiência produtiva é calculada a partir da seguinte lógica:*

***eficiência = produção total / volume total de fertilizante***

*Esse indicador representa quanto o talhão produziu em relação ao volume de fertilizante aplicado.*

*A classificação adotada no sistema é:*

- ***baixa**: índice menor que 2*
- ***média**: índice entre 2 e 5*
- ***alta**: índice maior ou igual a 5*


*Essa análise permite verificar se o uso do insumo está gerando retorno produtivo satisfatório.*


### 3. Classificação do risco ambiental

*O risco ambiental não é definido apenas pela produtividade, mas pelo equilíbrio entre **quantidade de insumo utilizada** e **eficiência obtida**.*

*A lógica adotada foi:*

- ***uso alto + eficiência baixa = risco alto***
- ***uso alto + eficiência alta = risco médio***
- ***uso baixo + eficiência alta = risco baixo***
- *todos os demais cenários = risco médio*


*Essa abordagem foi escolhida porque alta produtividade, sozinha, não garante sustentabilidade. Mesmo quando o resultado produtivo é positivo, o uso excessivo de fertilizantes pode representar pressão sobre o solo e o ambiente. Por isso, o sistema considera também o volume absoluto de insumos empregados.*


## 💬 Lógica por trás das recomendações do sistema

*Após classificar o uso de fertilizante, a eficiência produtiva e o risco ambiental, o sistema gera uma recomendação textual para orientar o usuário.*

*As recomendações seguem a seguinte lógica:*

### ✅ Manter a estratégia atual
*Gerada quando o talhão apresenta:*

- *uso de fertilizante **baixo***
- *eficiência produtiva **alta***
- *risco ambiental **baixo***

**Interpretação:**  
*Esse é o cenário mais equilibrado do sistema. O talhão apresenta bom retorno produtivo, sem depender de grande volume de insumos, indicando uma operação mais eficiente e sustentável.*


### ⚠️ Reduzir a intensidade de aplicação e revisar o manejo
*Gerada quando o talhão apresenta:*

- *uso de fertilizante **alto***
- *eficiência produtiva **baixa***
- *risco ambiental **alto***


**Interpretação:**  
*Esse é o cenário mais crítico. O sistema entende que há consumo excessivo de fertilizantes, mas sem retorno produtivo compatível. Isso sugere desperdício de insumos, baixa eficiência operacional e maior potencial de impacto ambiental.*


### 🌱 Manter o bom desempenho produtivo, mas avaliar alternativas para reduzir a dependência de fertilizantes
*Gerada quando o talhão apresenta:*

- *uso de fertilizante **alto***
- *eficiência produtiva **alta***
- *risco ambiental **médio***


**Interpretação:**  
*Neste caso, o talhão apresenta bom desempenho produtivo, porém depende de grande volume de insumos para atingir esse resultado. A recomendação não é interromper a estratégia imediatamente, mas buscar alternativas que mantenham a produtividade com menor dependência de fertilizantes.*


### 📉 Revisar o planejamento produtivo do talhão
*Gerada quando o talhão apresenta:*

- *uso de fertilizante **baixo***
- *eficiência produtiva **baixa***
- *risco ambiental **médio***


**Interpretação:**  
*Aqui o problema não está no excesso de insumo, mas na baixa resposta produtiva. Isso pode indicar necessidade de revisão do planejamento do talhão, da estratégia produtiva ou de outras variáveis não contempladas no protótipo.*


### 🔄 Monitorar o desempenho e ajustar gradualmente a estratégia
*Gerada para os cenários intermediários, que não se enquadram nas situações anteriores.*

**Interpretação:**  
*Essa recomendação foi criada para contextos em que o sistema identifica um desempenho mediano ou misto, sem caracterizar cenário ideal nem situação crítica. Nesses casos, a melhor orientação é acompanhar os resultados e promover ajustes progressivos.*


## 📝 Registro de logs em arquivo TXT

*Além do armazenamento em JSON e Oracle, o sistema também gera um **arquivo de log em TXT**, chamado `system_log.txt`.*

*Esse arquivo registra eventos importantes da aplicação, como:*

- *cadastro de talhão;*
- *exclusão de talhão;*
- *registro de aplicação de fertilizante;*
- *registro de produção;*
- *execução de análise;*
- *geração de recomendação sustentável.*


*Cada linha do log contém:*

- *data e hora do evento;*
- *tipo da ação realizada;*
- *detalhes resumidos da operação.*


### Exemplo de log:
*```txt
[21/04/2026 14:32:10] FIELD_REGISTERED: Field ID 1 registered - Name: Talhão Milho Norte, Area: 12.5, Crop: Milho*

## 🛠️ Tecnologias Utilizadas

*O projeto **AgroGreen Insight** foi desenvolvido utilizando Python e recursos essenciais da disciplina, aplicados de forma prática na solução proposta.*

*- **Python**: linguagem principal da aplicação, responsável pela lógica do sistema, validação de dados, análise e geração de recomendações.*


- ***Estruturas de Dados**:*
  - ***Listas e dicionários**: utilizados para armazenar e manipular os dados da aplicação;*
  - ***Tuplas**: utilizadas para representar classificações fixas (uso de fertilizante, eficiência e risco ambiental);*
  - ***Tabela de memória**: os dados são carregados dos arquivos JSON e manipulados em memória durante a execução.*

- ***Manipulação de Arquivos**:*
  - ***JSON**: utilizado para persistência dos dados do sistema (talhões, aplicações e produção);*
  - ***TXT**: utilizado para registro de logs das operações realizadas.*

- ***Banco de Dados Oracle**:*
  - *utilizado para persistência dos dados em formato relacional;*
  - *integração realizada via Python, com operações de criação, inserção, exclusão e consulta;*
  - *sincronização automática com os dados do JSON na inicialização do sistema.*


## 🔧 Como executar o código

*Pré-requisitos:*

*Git - Utilizado para clonar o repositório do projeto.*

*Visual Studio Code (VS Code) ou outra IDE/editor de sua preferência.*

*Python 3.10 ou superior - Utilizado no desenvolvimento da aplicação.*

*Biblioteca oracledb - Necessária para conexão com o banco de dados Oracle.*

*Banco de dados Oracle acessível - Utilizado para persistência dos dados.*


*Fase 1 — Clonar o repositório:*

*No terminal, execute:*

*git clone git@github.com:renatoruiz2607/agroGreenInsight.git*

*Em seguida, acesse a pasta do projeto:*

*cd agroGreenInsight*


*Fase 2 — Preparar o ambiente Python:*

*No terminal, verifique se o Python está instalado:*

*python3 --version*

*Instale a dependência do Oracle:*

*pip install oracledb*


*Fase 3 — Configurar conexão com o Oracle:*

*Configure as variáveis de ambiente com seus dados de acesso:*

*export ORACLE_USER=seu_usuario*

*export ORACLE_PASSWORD=sua_senha*

*export ORACLE_DSN=host:porta/service_name*


*Obs: é necessário ter acesso a um banco Oracle válido.*


*Fase 4 — Executar a aplicação:*

*No terminal, execute:*

*python src/main.py*

*ou execute o arquivo main.py pela IDE*


*Ao iniciar, o sistema irá:*

- *criar as tabelas no Oracle (caso não existam);*
- *sincronizar automaticamente os dados dos arquivos JSON para o banco;*
- *exibir um menu interativo no terminal.*


*Funcionalidades disponíveis no menu:*

- *cadastrar talhões*
- *listar talhões*
- *excluir talhões (com exclusão em cascata)*
- *registrar aplicações de fertilizante*
- *listar aplicações de fertilizante*
- *registrar produção*
- *listar produção*
- *analisar eficiência do talhão*
- *gerar recomendação sustentável*
- *encerrar o sistema*


## 🗃 Histórico de lançamentos

* 1.0.0 - 21/04/2026
    * 
* 0.9.0 - 21/04/2026
    * 
* 0.8.0 - 20/04/2026
    * 
* 0.7.0 - 20/04/2026
    * 
* 0.6.0 - 20/04/2026
    * 
* 0.5.0 - 20/04/2026
    * 
* 0.4.0 - 20/04/2026
    * 
* 0.3.0 - 20/04/2026
    * 
* 0.2.0 - 19/04/2026
    * 
* 0.1.0 - 19/04/2026
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


