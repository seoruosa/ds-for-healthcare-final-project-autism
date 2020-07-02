# ds-for-healthcare-final-project-autism
Final project about autism for discipline of Data Science and Visualization in Healthcare

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/seoruosa/ds-for-healthcare-final-project-autism/master)

### Links
* https://blog.ouseful.info/2019/12/10/accessing-mybinder-kernels-remotely-from-ipython-magic-and-from-vs-code/

#### Git commands
Ignore changes on a file
    git update-index --assume-unchanged credentials.py
Return to consider modifications
    git update-index --no-assume-unchanged credentials.py

#### Github configurations to use Google Colab
* https://towardsdatascience.com/google-drive-google-colab-github-dont-just-read-do-it-5554d5824228


### GEPHI: Instalation and running
    docker pull dit4c/dit4c-container-gephi
    docker run -p 8080:8080 dit4c/dit4c-container-gephi

#### passo a passo de analise de dados
* como mostrar a correlação
  * ~~mostrar a correlacao de todas as variaveis e das excluidas~~
  * ~~outros tipos de correlacao q lidam com nan~~ -> a kendall é muito lenta 
  * ~~mudar cor de pontos~~
  * ~~tirar nomes da parte de baixo do grafico~~
  * ~~mudar a cor do grafico~~

* analise dos dados / analise exploratoria
  * quantos nan temos em cada coluna
  * contagem de respostas

* outra funcao para calcular score de dados desbalanceados
  * make_score(recal_score, **kwargs)
