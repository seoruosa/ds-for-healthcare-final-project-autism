# Bem-vindo!
Você está no repositório referente ao projeto final com o tema de **diagnóstico de autismo** da matéria de Ciência e Visualização de Dados em Saúde na UNICAMP desenvolvido por Gabriela Servidone (gabi.servidone@gmail.com), Felipe Labate e Thiago Giachetto de Araujo (thiago.giachetto@gmail.com). Abaixo explicamos um pouco mais sobre o tema, ferramentas utilizadas, a modelagem desenvolvida, como também seus resultados e conclusões. 

## O Autismo e seu Diagnóstico
Ainda existem muitas discussões em relação à quem foi o primeiro a descobrir e oficializar as descrições iniciais do autismo, já que, de acordo com Chown [2], Aspenger e Kanner publicaram suas descobertas em anos consecutivos e, à principio, sem ter conhecimento do trabalho do outro. 

Independentemente de quem foi o primeiro, ambos continuaram seus estudos na área, e em 1943, Kanner publicou "Autistic Disturbances of Affective Contact" [1] com comentários sobre as 11 crianças com semelhanças comportamentais marcantes que havia encontrado até então, sendo Donald Gray Triplett a primeira criança diagnosticada oficialmente como autista [3].  

Em 1952, foi publicada a primeira versão Diagnóstico e Estatístico de Transtornos Mentais (DSM-1) [7], documento que trouxe uma uniformização do sistema de classificação dos transtornos mentais, tornando-se um manual para profissionais da área, incluindo, então, a primeira definição oficial de como diagnosticar o autismo. 

De edição em edição, as classificações de transtornos mentais são atualizadas, e, por haver uma grande diversidade na expressão clínica de indivíduos autistas, em sua quinta versão, o Diagnóstico e Estatístico de Transtornos Mentais [6] optou por usar a palavra "*espectro*" para a definição de 2014, agora conhecida como: **transtorno do espectro do autismo** (TEA). 

Além disso, vale ressaltar que mesmo em 2014 onde já haviam estudos que buscavam correlacionar fatores genéticos com o autismo [4,5], desde Triplett, o diagnóstico continua puramente clínico, se baseando completamente no comportamental do indivíduo.  

Com base nos fatos acima, nosso estudo tem como objetivo inicial **prover uma nova ferramenta aos profissionais da área que os ajudaria num diagnóstico mais eficaz**.

## Ferramentas Utilizadas
Abaixo, listamos as ferramentas utilizadas para o desenvolvimento e organização de nossa equipe de projeto. 

 - **Google Drive:** O Google Drive foi utilizado como um banco geral de informações e arquivos, nele foram armazenados os artigos relativos ao tema, pelo Drive temos o acesso aos notebooks do Google Colaboratory, à nossa base de dados privada, entre outros arquivos.  
- **Google Scholar:** Os artigos referenciados aqui, foram descobertos principalmente via Google Scholar. As palavras-chave principais utilizadas foram: autistic; autism; history; kanner; checklist. 
- **Google Colaboratory:** As análises e modelagem desenvolvidas para este estudo, foram inteiramente em notebooks Pyhton dentro do Colab.
- **StackEdit:** Esta aplicação foi utilizada para a escrita dos readme's utilizados e comitados em nosso [repositório](https://github.com/seoruosa/ds-for-healthcare-final-project-autism).  É uma ferramenta opensource online e didática.
- **GitHub:** Para a estruturação base de todos os arquivos de nosso projeto, utilizamos o GitHub.

> **Mendeley:** Inicialmente começamos utilizando o Mendeley como um banco de artigos sobre o tema, porém, descontinuamos e focamos utilizar o Google Drive de uma maneira mais centralizada.  

## A Modelagem
Outro ferramental teórico utilizado no desenvolvimento desta modelagem, é o método **Knowledge Discovery in Database** (KDD), ou seja, Descoberta de Conhecimento em Banco de Dados. Tal como Usama Fayyad descreve [8], o processo KDD está preocupado em desenvolver metodologias e técnicas para entender os dados, seja quais eles forem, entretanto, comumente utilizado em desenvolvimentos de grande volumetria de dados. 

O processo KDD é composto por uma série de etapas sequenciais, porém é iterativo, ou seja, a qualquer passo, pode haver retorno a etapas anteriores.  

![enter image description here](https://github.com/seoruosa/ds-for-healthcare-final-project-autism/blob/master/assets/fayad.png)

### Seleção
Para este estudo, estaremos utilizando o *survey* anual da *Data Resource Center for Child & Adolescent Health* (DRC) chamado **National Survey of Children's Health** (NSCH). A pesquisa fornece dados ricos sobre vários aspectos da vida das crianças Norte Americanas, incluindo informações como: saúde física e mental, informações sobre os cuidados de saúde, histórico familiar, sobre sua vizinhança, escola, como também o contexto social da criança está inserida. Para ter acesso aos dados, é necessário acessar este [site](https://www.childhealthdata.org/dataset), e preencher o formulário de aceite dos termos de sigilo de dados. 

Uma das características desse banco de dados, é que a pesquisa tem atualizações em suas perguntas quase anualmente, consequentemente, as informações entre anos, não necessariamente se conversam. Por este motivo, optamos por utilizar um único arquivo disponibilizado pelo DRC que contempla os anos 2017 e 2018 [9].

A base de dados "*2017-2018 National Survey of Children's Health (NSCH)*" tem inicialmente 745 perguntas e 52.129 registros, desses 1.345 registros responderam que "Sim" na pergunta "*Autism ASD Currently*".
  
### Pré-processamento
O NSCH tem muitas perguntas em cadeia, ou seja, perguntas que só são respondidas via um fator condicionante da pergunta anterior, que quando não são respondidas, recebem valores como: 90, 95, 96 e 99. Para estes campos, atualizamos seus valores para NaN's. 

Começamos, então, a avaliar quais variáveis utilizaríamos para treinar os modelos de classificação. Porém, como o NSCH é uma pesquisa bem completa, ela já inclui algumas perguntas do *checklist* [6] utilizado para o diagnóstico do TEA. Considerar essas variáveis para o treinamento do modelo, vai contra o objetivo do estudo, que é descobrir se é possível desenvolver um classificador novo, logo, uma primeira limpeza foi retirar variáveis que continham 'screener', 'asd', 'autism', 'sc ', 'cshcn' ou 'indicator' em sua descrição. 

Além disso, calculamos a correlação de Spearman de as todas as variáveis versus a variável "*Autism ASD Currently*". E tal como pode ser visto no gráfico abaixo, uma grande maioria das perguntas tinha uma correlação abaixo de 0.1 com "*Autism ASD Currently*", estas também foram excluídas. 
    
![enter image description here](https://github.com/seoruosa/ds-for-healthcare-final-project-autism/blob/master/assets/correlation.png)

### Transformação
O último passo antes do treinamento dos modelos que serão descritos a seguir, foi a tradução dos "*not a number*" (NaN) para um valor numérico, "999". 

### Mineração de Dados

    aqui eu acho que se falar um pouco dos modelos, da parte de balanceamento 

Observando os dados pode-se verificar que boa parte das questões não eram respondidas por todos os entrevistados, o que implica que temos muitos dados vazios e a quantidade de perguntas realizadas no censo, também é bem grande (744). Além disso, outra dificuldade é que os dados são muito desbalanceados já que das 52129 entrevistas, somente 1345 são de crianças diagnosticadas com ASD ou autismo. 

Para tentar lidar com esses pontos de dificuldade tentamos utilizar algumas estratégias de seleção de variável. Além da retirada das variáveis com baixa correlação e utilizamos algum modelo baseado em árvore para podarmos algumas variáveis e depois usamos outro modelo para fazer a classificação. Também fizemos um teste, utilizando somente Random Forest, mas o resultado foi aquém ao obtido com a etapa de seleção de variável.

Além disso, para lidar com o desbalanceamento, testamos a utilização de oversampling dos dados de crianças diagnosticadas com ASD, adicionando linhas através de um sorteio com reposição dos dados dessa classe, de tal forma que as duas classes tivessem o mesmo número de elementos. 

    Utilizando essa metodologia, observamos que a precisão aumento bastante, porém o f1-score foi bem baixo



<center>

|feature selection                    |classifier                |precision*|recall*   |f1-score*|Oversampling|
|-------------------------------------|--------------------------|----------|----------|---------|------------|
|Random Forest***                     |Support Vector Machine    |0.82      |0.62      |0.67     |N           |
|Decision Tree Classifier(\*\*\*)     |Support Vector Machine    |0.49      |0.50      |0.49     |N           |
|Decision Tree Classifier(\*\*)       |Logistic Regression       |0.79      |0.64      |0.69     |N           |
|**Decision Tree Classifier(\*\*\*)** |**Logistic Regression**   |**0.73**  |**0.67**  |**0.69** |**N**       |
|                                     |Random Forest(\*\*\*\*)   |0.81      |0.62      |0.67     |N           |
|                                     |Random Forest(\*\*\*\*)   |0.93      |0.51      |0.51     |Y           |
|Random Forest(\*\*\*)                |Support Vector Machine    |0.81      |0.62      |0.67     |Y           |

</center>
(\*) Macro average ([link](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score))
(\*\*) with threshold value
(\*\*\*) with threshold value and max_features 
(\*\*\*\*) using balanced class weight for training score

Os valores de *f1-score* que os modelos desenvolvidos obtiveram, mostram que nenhum se destacou positivamente, escolhemos, então, para aprofundarmos as análises o ressaltado em **negrito**.  O treinamento do modelo via *Decision Tree Classifier* e *Logistic Regression* utilizou as perguntas do NSCH abaixo.

ID|Variável|Descrição|
|--|---------------------------------|--------------------------|
1| ANYOTHER |  Any Other Condition|
2| CSHCNComplex_1718 |  Complexity of health care needs|
3| MENBEVCOV   |Health Insurance - Cover Mental Behavioral Needs|
4| K4Q38   |Received Special Services - Currently
5| ARRANGEHC   |Hours Spent Arranging Health Medical Care
6| K5Q21   |Arrange Or Coordinate Care Extra Help
7| TOTNONSHCN|   Count of Children without Special Health Care Needs in Household
8| partic_1718|   Number of organized activities child participates in after school (6-17 years)
9| EMOSUPADV|   Emotional Support - Health Condition Support Group
10| SESPLANYR|   Special Education Plan - Age in Years
11| K4Q26  | Specialist Visit - Problem
12| K2Q33C|   Anxiety Severity Description
13| K5Q11 |  Need a Referral - Problem
14| K8Q32 |  How Often Have You Felt - Child Really Bothers You
15| K2Q01 |  General Health
16| C4Q04 |  Frustrated In Efforts to Get Service
17| K8Q21 |  Share Ideas or Talk About Things That Matter
18| K7Q85_R|   Stays Calm and In Control When Challenged
19| cntdiff  | Number of functional difficulties reported from list of 12 different difficulties asked in the survey
20| ADHDSev_1718|   Parent-rated severity of child's current ADD/ADHD, age 3-17 years
21| K8Q31   |How Often Have You Felt - Child Hard to Care For
22| HCEXTENT|   Health Affected Ability - Extent
23| CondCnt27_1718|   Number of current health conditions reported from a list of 27
24| speech_1718   |Children who currently have speech or other language disorder, age 3-17 years
25| MAKEFRIEND   |Difficulty Making or Keeping Friends

### Interpretação e Avaliação
Dentre os métodos atuais para identificação do TEA, a Sociedade Brasileira de Pediatria recomenda o  _Modified Checklist for Autism in Toddlers_ (M-CHAT). Ele é um instrumento composto de 23 perguntas [11], um número similar às 25 variáveis de nosso modelo final. Entretanto, 

> **É possível criar um classificador de pessoas autistas via perguntas específicas?**

    sim, porem que nao necessariamente é melhor que o mchat, sobre o que é o mchat 

> **Existe correlação entre as respostas dos formulários e a classificação do paciente?**

    falar que sim, e que foram essas as variaveis que foram utilizadas para o treinamento dos modelos acima 

> **Como especialistas classificam se uma pessoa é ou não autista?**

De acordo com o _Diagnostic and Statistical Manual of Mental Disorders_ (DSM-5) [6], o diagnóstico do Transtorno do Espectro Autista é baseado em cinco critérios, apresentados sucintamente a seguir:

 1. “Déficits persistentes na comunicação social e na interação social em múltiplos contextos (...)
 2. Padrões restritos e repetitivos de comportamento, interesses ou atividades (...)
 3. Os sintomas devem estar presentes precocemente no período do desenvolvimento (...)
 4. Os sintomas causam prejuízo clinicamente significativo no funcionamento social, profissional ou em outras áreas importantes da vida do indivíduo no presente (...)
 5. Essas perturbações não são mais bem explicadas por deficiência intelectual (transtorno do desenvolvimento intelectual) ou por atraso global do desenvolvimento (...)”

Além disso, muitos indivíduos com transtorno do espectro autista apresentam também o comprometimento da linguagem, da capacidade intelectual e de habilidades funcionais. Os diagnósticos - quando baseados em múltiplas fontes de informação, como observações clínicas, relatos de cuidadores, e quando possível, de autorrelato – se tornam mais confiáveis e válidos.

**Dificuldades Enfrentadas:** De maneira geral, tivemos duas dificuldades maiores durante a execução do projeto. A primeira delas foi causada diretamente pela escolha da base de dados, porque, pelos motivos e detalhamentos já descritos acima, a base de dados utilizada neste estudo é privada. Logo, fomos limitados a não utilizar plataformas públicas de desenvolvimento, como Binder, que era a ideia inicial.  O segundo ponto que tivemos dificuldades, foi encontrar psicólogos ou psicologas especialistas em autismo para nos auxiliar nos entendimentos iniciais e conclusões. 

**Mudanças de Percurso:** Ao início do projeto, montamos um cronograma geral das macro atividades a serem feitas, tal como imagem abaixo. Nota-se que planejamos que as tarefas fossem feitas de uma maneira linear dentre as semanas, porém, por motivos externos e particulares, infelizmente não conseguimos seguir nosso planejamento à risca, e mudamos nosso cronograma algumas vezes dentro deste período. 

![Cronograma Inicial](https://github.com/seoruosa/ds-for-healthcare-final-project-autism/blob/master/assets/schedule.jpeg)

**Lições Aprendidas:**

## Comentário da Psicóloga



## Trabalhos Futuros
No final do século XX começou-se a estudar a relação entre o Transtorno do Espectro Autista e a genética, e foi concluído que o TEA é o distúrbio neuropsiquiátrico com o maior componente genético [10]. Com o passar do tempo foram sendo construídas bases de dados em volta das pesquisas envolvendo essa relação, como por exemplo a [SFARI Gene](https://gene.sfari.org/) que é uma coleção dos genes implicados na suscetibilidade ao autismo.

Uma ideia para um trabalho futuro seria procurar um modelo que combine as perguntas comportamentais, que já são feitas atualmente, com os fatores genéticos de pacientes. Tal modelo poderia ser usado para se obter um melhor, mais preciso e confiável diagnóstico.

    falar sobre uma comparação com as perguntas desse projeto versus o mchat
    o modelo te devolver faixas de risco e não um sim/não

## Agradecimentos
Agradecemos aos professores André Santanchè (IC-UNICAMP) e Paula Dornhofer (FEEC-UNICAMP) pelo ensino da matéria de Ciência e Visualização de Dados em Saúde que nos proporcionou o desenvolvimento deste projeto. 

Agradecemos também à Juliana Tortorelli, psicóloga, pelas referências locais de tratamento de autismo e participação. 

## Referências
[1] Kanner, Leo. "Autistic disturbances of affective contact." _Nervous child_ 2.3 (1943): 217-250.

[2] Chown, Nick, and Liz Hughes. "History and first descriptions of autism: Asperger versus Kanner revisited." _Journal of autism and developmental disorders_ 46.6 (2016): 2270-2272.

[3] Pallardy R. ["Donald Triplett"](https://www.britannica.com/biography/Donald-Triplett). _Encyclopædia Britannica_. Retrieved  19 March  2017.

[4] Marshall, Michael. ["The hidden links between mental disorders."](https://www.nature.com/articles/d41586-020-00922-8) *Nature* 581 (2020), 19-21.

[5] Ronald, Angelica, et al. "Evidence for overlapping genetic influences on autistic and ADHD behaviours in a community twin sample." _Journal of Child psychology and Psychiatry_ 49.5 (2008): 535-542.

[6] Associação Americana de Psiquiatria, APA. DSM V – Manual diagnóstico e estatístico de transtornos mentais. 5. ed.rev. – Porto Alegre: *Artmed*, 2014.

[7] Associação Americana de Psiquiatria, APA. DSM I – Manual diagnóstico e estatístico de transtornos mentais. 1. ed.rev. –Washington, DC: *American Psychiatric Association,* 1952.

[8] Fayyad, Usama M., Gregory Piatetsky-Shapiro, and Padhraic Smyth. "Knowledge Discovery and Data Mining: Towards a Unifying Framework." _KDD_. Vol. 96. 1996.

[9] Child and Adolescent Health Measurement Initiative (CAHMI) (2017-2018). 2017-2018 National Survey of Children's Health, [(SAS/SPSS/Stata)] Indicator Data Set. Data Resource Center for Child and Adolescent Health supported by Cooperative Agreement U59MC27866 from the U.S. Department of Health and Human Services, Health Resources and Services Administration (HRSA), Maternal and Child Health Bureau (MCHB). Retrieved [09/05/2020] from childhealthdata.org.

[10] Persico, Antonio M., and Valerio Napolioni. "Autism genetics." *Behavioural brain research* 251 (2013): 95-112.

[11] Robins DL, Fein D, Barton ML, Green JA. "The Modified Checklist for Autism in Toddlers: an initial study investigating the early detection of autism and pervasive developmental disorders." *J Autism Dev Disord* 31(2) (2001): 131-44.
