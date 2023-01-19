from collections import defaultdict, Counter

aparicoes = {
    "Felipe": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

# print(aparicoes["Felipe"])

aparicoes["bem"] = 1
del aparicoes["nome"]

# print(aparicoes)

for chave, valor in aparicoes.items():
  # print(chave, "=", valor)
  pass
  
palavras = defaultdict(int)

texto = "Bem vindo meu nome é Felipe e eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
texto = texto.lower()

for palavra in texto.split():
  palavras[palavra] += 1
  
# print(palavras)

class Conta:
  def __init__(self):
    # print("Imprimindo conta")
    pass
    
contas = defaultdict(Conta)
contas[15]

palavras = Counter(texto.split())
# print(palavras)

texto1 = """
Se você está começando a aprender sobre desenvolvimento de software, provavelmente já ouviu falar sobre React. Mas o que é esse framework e por que é tão popular entre pessoas desenvolvedoras?

Você como pessoa usuária de redes sociais, principalmente do ecossistema do Facebook, já deve ter percebido que determinadas partes da tela tem comportamentos especiais ou independentes do restante da aplicação. Por exemplo, os anúncios que são exibidos.

Pensando na melhor forma de lidar com esse tipo de funcionalidade, a equipe de desenvolvedores do Facebook desenvolveu uma forma muito específica de lidar com os dados exibidos e a atualização dessas pequenas porções da aplicação: o React.

Muitas empresas de tecnologia, incluindo o Instagram, a Netflix, o Airbnb e o Twitter, usam o React em suas aplicações web e móveis. Isso significa que há uma grande variedade de oportunidades de emprego em diferentes tipos de empresas que usam React.

Além disso, o React é uma biblioteca de código aberto, o que significa que há uma comunidade ativa e vibrante de desenvolvedores que contribuem com código e recursos para ajudar a melhorar a tecnologia. Isso pode ser uma ótima maneira de se conectar com outros desenvolvedores e aprender sobre as últimas tendências e melhores práticas no mundo do React.

Em resumo, o mercado de trabalho para desenvolvedores React é muito bom, com muitas empresas de tecnologia que usam essa tecnologia em suas aplicações. Além disso, a comunidade de código aberto do React é ativa e oferece muitas oportunidades de aprendizado e networking.

Neste artigo, você descobrirá o que é React, para que serve e como mergulhar mais fundo nesse universo do front-end.

O que é?
React é um framework JavaScript criado pelo Facebook (atual Meta) que é usado para criar interfaces de usuário (UI) em aplicativos web. Ele é popular por ser fácil de usar, altamente flexível e escalável, e é usado por muitas empresas de tecnologia, incluindo o Facebook, Instagram e Airbnb.

Framework?
Um framework é um conjunto de ferramentas e bibliotecas que fornecem um conjunto de recursos e funcionalidades prontas para desenvolvedores de software. Isso permite que eles construam aplicativos mais rapidamente, com menos esforço e código, e com menos chance de erros.

Existem vários frameworks diferentes disponíveis para diferentes linguagens de programação, incluindo JavaScript, Python, Java e muitas outras. Alguns dos frameworks mais populares incluem o React para JavaScript, o Django para Python e o Spring para Java.

O React é uma linguagem de programação?
A resposta é simples: não! O React não pode ser considerado uma linguagem de programação como JavaScript, Java e .net; trata-se de um framework, conforme vimos.

Principais caso de uso do React
Um dos principais casos de uso do React é criar aplicações web complexas que precisam ser atualizadas em tempo real. Por exemplo, o Facebook usa o React para criar sua interface de usuário, que precisa ser atualizada constantemente com novas informações de amigos, mensagens, e notificações. O React é ideal para esse tipo de aplicação porque ele permite que você atualize a interface de usuário de forma rápida e eficiente.

Outro caso de uso comum do React é criar aplicações web que precisam ser escaláveis e mantidas por equipes grandes. O React é uma biblioteca modular, o que significa que os componentes podem ser facilmente reutilizados e compartilhados entre diferentes partes da aplicação. Isso torna mais fácil manter e expandir uma aplicação à medida que ela cresce, e permite que equipes de desenvolvimento trabalhem de forma mais eficiente juntas.

Além disso, o React é frequentemente usado em conjunto com o React Native para criar aplicações móveis nativas para iOS e Android. Isso permite que você crie aplicações móveis de alta qualidade que se sentem e se comportam como aplicações nativas, mas são construídas usando tecnologias web, como JavaScript e CSS.

React e React Native são a mesma coisa?
A principal diferença entre o React e o React Native é o tipo de aplicação que eles criam. O React é usado para criar aplicações web, enquanto o React Native é usado para criar aplicações móveis. No entanto, ambos compartilham muitos conceitos e sintaxe, então se você é familiarizado com o React, será mais fácil aprender o React Native.

Em resumo, React e React Native são ferramentas diferentes, mas relacionadas. O React é usado para criar aplicações web, enquanto o React Native é usado para criar aplicações móveis. No entanto, ambos compartilham muitos conceitos e sintaxe, então é possível usar o conhecimento de um para aprender o outro.

Quais são os pré-requisitos para que eu possa ter uma boa curva de aprendizado em React?
Antes de começar a aprender React usando componentes funcionais, é importante ter algum conhecimento básico de JavaScript. React é uma biblioteca de JavaScript, então é fundamental entender como essa linguagem funciona para poder usar o React de forma eficiente. Isso inclui coisas como variáveis, funções, loops, e condicionais.

Além disso, é importante ter alguma familiaridade com o HTML e o CSS. React é usado principalmente para criar interfaces de usuário, então é preciso saber como estruturar e estilizar um documento HTML para poder criar componentes visuais interessantes.

Outra coisa que pode ser útil antes de começar a aprender React usando componentes funcionais é ter algum conhecimento de programação funcional. Os componentes funcionais se baseiam em funções, então é importante entender como elas funcionam e como elas podem ser usadas para construir aplicações. Isso inclui coisas como closures e higher-order functions.

Em resumo, antes de começar a aprender React usando componentes funcionais, é importante ter algum conhecimento básico de JavaScript, HTML e CSS, e programação funcional. Isso vai tornar o aprendizado do React mais fácil e mais eficiente.

Preciso aprender JavaScript antes de aprender React?
React é um framework JavaScript, o que significa que ele é construído em cima da linguagem JavaScript e depende dela para funcionar. Isso significa que se você quiser usar o React para criar aplicativos, é fundamental que você entenda os conceitos básicos e as sintaxes do JavaScript.

Inclusive, aqui na Alura, existe essa formação focada em JavaScript. Onde o foco é a criação de páginas web de maneira que você tenha a base necessária para estudar os frameworks mais famosos do mercado, incluindo o React.

Além disso, o React é baseado em alguns conceitos avançados do JavaScript, como a manipulação de eventos, a criação de funções de callback e a manipulação do DOM (Document Object Model). Se você não entender esses conceitos, pode ser difícil acompanhar o código do React e usá-lo de forma eficiente.

Portanto, se você está interessado em aprender React, é importante que você primeiro aprenda e compreenda os conceitos básicos do JavaScript. Isso lhe dará as bases para usar o React de forma eficiente e criar aplicativos incríveis.

Comece seus primeiros passos no React
Acesse gratuitamente as primeiras aulas de React da Formação React com JavaScript da Alura e aprenda mais sobre:

O que é o React
Gerenciamento de estado
Manipulação de arquivos estáticos
Testes automatizados
Single Page Applications
Inclusive, eu gravei junto do Paulo Silveira o primeiro curso da formação, num formato bem diferente e que a comunidade de alunos e alunas da Alura tem gostado demais!

Por que utilizar React?
Aqui estão algumas razões pelas quais aprender React pode ser valioso para sua carreira como desenvolvedor:

É popular e amplamente utilizado
O React.JS é um dos frameworks JavaScript mais populares e amplamente utilizados em todo o mundo. Ele é usado por muitas empresas de tecnologia, incluindo o Facebook, Instagram e Airbnb, e é adotado por desenvolvedores em todos os tipos de projetos. Isso significa que o React é uma opção confiável e bem suportada para o seu projeto.

Oferece muitos recursos e ferramentas úteis
O React.JS oferece muitos recursos e ferramentas úteis que tornam o desenvolvimento de aplicativos web mais fácil e eficiente. Isso inclui bibliotecas de componentes prontos para uso.

Como funciona o React?
Já sabemos que o React usa a linguagem JavaScript para criar componentes, que são pequenos pedaços de código que representam uma parte específica da interface do usuário (UI) de um aplicativo. Cada componente tem um estado, que é uma variável que armazena as informações que mudam dentro do componente, como os dados de um formulário ou a cor de um botão.

Quando o usuário interage com o aplicativo, como clicar em um botão ou preencher um formulário, o estado dos componentes é atualizado e reflete as mudanças na UI. Isso é feito com o uso de funções de callback, que são funções que são chamadas quando uma ação é executada pelo usuário.

O React também usa o que é chamado de "Virtual DOM" (Document Object Model Virtual), que é uma representação em memória da UI do aplicativo. Quando o estado dos componentes muda, o Virtual DOM é atualizado e comparado com o DOM real para determinar quais mudanças precisam ser feitas na UI. Isso é muito mais rápido do que atualizar o DOM diretamente, o que torna o React.JS muito rápido e eficiente.

DOM e Virtual DOM
O DOM, ou "Document Object Model", é uma representação em árvore de um documento HTML ou XML. Ele é usado pelo navegador para entender o conteúdo de uma página web e permitir que o usuário interaja com ela.

Por exemplo, quando você clica em um botão em uma página web, o navegador usa o DOM para entender o que deve acontecer. Ele procura o elemento HTML correspondente ao botão no DOM, e depois executa a ação especificada pelo desenvolvedor.

O problema é que o DOM pode ser lento para atualizar e manipular. Ele é uma representação direta da página web, então qualquer alteração nos dados da página requer uma atualização completa do DOM. Isso pode ser muito lento para aplicações web mais complexas, que podem ter milhares ou até milhões de elementos HTML.

Para resolver esse problema, o React introduziu o Virtual DOM. O Virtual DOM é uma representação em memória do DOM, que é atualizada muito mais rapidamente do que o DOM real. Quando um componente do React é atualizado, o Virtual DOM é atualizado primeiro, e depois as alterações são sincronizadas com o DOM real. Isso torna a atualização da interface de usuário muito mais rápida e eficiente.

Em resumo, o DOM é a representação de um documento HTML ou XML no navegador, enquanto o Virtual DOM é uma representação em memória do DOM que é usada pelo React para atualizar a interface de usuário de forma mais rápida e eficiente.
"""

texto2 = """
Introdução: Trello e Produtividade
Para entendermos por que seu time precisa conhecer o Trello, vamos conhecer a Maria, que já realizou alguns trabalhos de maneira individual, mas foi contratada para trabalhar em equipe na empresa Bytestore. Ela e seu time têm algumas dúvidas sobre como dividir as tarefas de um projeto, definir prazos, responsáveis e priorizar o que é mais importante a ser executado.

Ao pesquisarem sobre ferramentas para aumentar a produtividade, as pessoas da equipe de Maria encontraram o Trello. Descobriram que ele pode ser usado para facilitar o gerenciamento de projetos, e melhorar a forma de lidar com o fluxo de informações e a gestão dos negócios. Assim, para ajudarmos a Maria, vamos aprender mais sobre essa ferramenta e entender as vantagens de usá-la na sua equipe.

Observação: o exemplo de Maria se aplica tanto para quem está na primeira interação com o Trello, quanto para pessoas mais experientes no assunto de produtividade.

O que é Trello? Conhecendo a ferramenta
O Trello é uma ferramenta que oferece um plano gratuito para organizar desde nossas tarefas pessoais até demandas coletivas de uma equipe. Ele possibilita que criemos quadros com listas e adicionemos nelas cartões – ou cards, como costumamos dizer no dia a dia – com itens e tarefas, que são úteis para organizar times e atividades específicas para um determinado conjunto de pessoas.

Vamos conferir na prática como funciona um quadro e encontrar as melhores funcionalidades para Maria e a sua equipe. Na imagem abaixo, temos um exemplo de um quadro de atividades estruturado no Trello.

Trello: como funciona os quadros
Quadro do Trello e o Método Kanban
No quadro do Trello, temos as seguintes colunas, ou etapas das atividades:

Backlog;
A fazer;
Em andamento;
Concluído.
Esta divisão contribui para a gestão visual, facilitando o acompanhamento das tarefas por meio de cards móveis que contêm a descrição de cada atividade e de evolução de projeto.

Assim, se um membro do time de Maria escolher uma atividade para fazer, esta pessoa deve mover o card, seguindo o fluxo de trabalho utilizado no Kanban.

O card inicia na coluna Backlog, e, à medida que é atualizado, transita pelas colunas de A Fazer, Em Andamento e, por fim, Concluído. Essa é uma forma de acompanhar o andamento do fluxo de atividades e suas respectivas informações, como demostrado no GIF a seguir:

Vantagens do Trello
Como essa ferramenta pode melhorar o dia a dia da equipe que Maria faz parte?
Uma grande vantagem do Trello para o trabalho em equipe são as atualizações colaborativas em tempo real. Então, se a Maria realizar uma mudança no quadro, todos os outros membros poderão acompanhar essa atualização de imediato. Tudo isso, apenas olhando o quadro, que mostra de forma resumida o andamento do projeto. Cada card também contém o histórico de alterações realizadas pelos membros.

Além disso, o Trello possui diversas funcionalidades para organização, como o uso de datas, lembretes e notificações para cartões de atividades, etiquetas, ingresso de membros, checklists e power-ups, como podemos observar na imagem abaixo:

Outra grande vantagem do Trello, é que ele pode ser utilizado em diferentes contextos, não apenas para a situação da Maria e equipe.

Portanto, cabe a você decidir quais funcionalidades fazem mais sentido para você no seu dia a dia.

Funcionalidades do Trello
1. Datas, lembretes e notificações
Por trabalhar constantemente com prazos, é interessante para o time de Maria ter fácil visualização do que está em espera, em execução e entregue. Isso é útil para evitar atrasos que possam atrapalhar o time no objetivo de concluir uma determinada tarefa.

O Trello permite que você determine uma data de início e uma data de entrega daquela tarefa, e também quando uma pessoa do time deverá receber um lembrete sobre o prazo da atividade.

2. Etiquetas
Com o Trello você pode adicionar etiquetas para categorizar as tarefas que foram criadas. Essas etiquetas podem possuir nomes e cores diferentes, auxiliando a equipe na organização de suas atividades.

3. Membros
O time da Maria trabalha com uma divisão de atividades por pessoa. E no Trello, utilizando a funcionalidade de Membros, é possível atribuir determinada tarefa a uma ou mais pessoas específicas do time.

Quando Maria ingressa em um card como membro, ela também recebe notificações por e-mail ou pelo aplicativo para dispositivos móveis do Trello, de quaisquer alterações que sejam feitas no card, sendo útil também para acompanhar o andamento daquela tarefa quando esta for compartilhada com mais pessoas.

4. Checklists
Os checklists são utilizados quando o time da Maria precisa detalhar os passos de uma tarefa e/ou sequências de ações que precisam ser marcadas como concluídas. Considere o exemplo da imagem acima.

No caso da produção do artigo, essa tarefa pode ser dividida em três partes: criação, revisão e publicação. Cada parte seria um item a ser concluído no checklist. O Trello também permite a criação de vários checklists no mesmo cartão.

5. Power-Ups
Uma outra funcionalidade do Trello são os power-ups, ou Superpoderes, que integram em um só local, nesse caso, o Trello. As ferramentas que o time da Maria já utilizava de outras maneiras, como: Calendários, Cronômetros, Agenda, Contadores, entre outros, agora estão disponíveis e tornam o trabalho em equipe muito mais fluido.

Também é possível escolher quais e quantos power-ups adicionar. Alguns exemplos relacionados às atividades associadas a Maria que podem ser feitos com os power-ups são:

Criar um calendário para visualizar todas as datas de entrega dos seus cards;
Exibir e anexar seus arquivos do Google Drive;
Criar votações nos cards em tempo real;
Automatizar tarefas;
Adicionar detalhes visuais para personalizar os quadros;
E muito mais!
Mas lembre-se que nem todos os power-ups são gratuitos, então é importante conferir para cada uso.

Outros recursos interessantes
Compartilhamento de documentos
O Trello possui a grande vantagem de aceitar diferentes formas de anexo, onde você pode disponibilizar no card da sua tarefa diferentes documentos em vários formatos, seja ele pdf, mp4, png, dentre outros. Assim, todos do time conseguem ver os documentos envolvidos no projeto que você está trabalhando.

O limite de espaço para armazenamento varia de acordo com o plano utilizado. Confira as informações de planos disponíveis no Trello, com respectivos preços e permissões.

Comentários
Através dos comentários dentro de cada card as ações podem ser documentadas, de forma que informações sobre o projeto não sejam perdidas.

Menções
As menções são importantes para fazer chamadas de atenção para um membro ou conjunto de pessoas específicas. Ao se utilizar o caractere @ seguido do nome de usuário, o membro recebe uma notificação para aquele local. No Trello, você pode fazer menções nos cards, checklists e comentários.

Filtros e atalhos
O filtro é uma ferramenta útil para consulta de cards no Trello, onde é possível verificar de forma rápida os cards que envolvem determinadas palavras-chave, membros, datas de entrega, etiquetas e muito mais.

O Trello também disponibiliza atalhos que podem facilitar o filtro de cards, entre outras ações.

Conclusão
Nesse artigo, você conheceu um pouco sobre como o Trello pode auxiliar no trabalho de pessoas desenvolvedoras como a Maria, e também viu poderosos recursos para dividir as tarefas de um projeto, definir prazos, delegar responsabilidades e priorizar o que é mais importante a ser executado em equipe.

Além disso, também vimos que o Trello pode ser aplicado em diferentes contextos e situações, devido à grande quantidade de funcionalidades disponíveis e também à sua flexibilidade de operação, que pode auxiliar no dia a dia tanto de uma pessoa, de um projeto, quanto de uma equipe inteira de trabalho.

Produtividade e as Ferramentas para a sua Carreira
E o aprendizado não para por aqui! Para continuar evoluindo seus estudos sobre produtividade, deixamos como indicação o Podcast do Hipsters Tech sobre Trello e outras ferramentas de produtividade, que conta um pouco mais sobre organização e sobre algumas outras ferramentas, inclusive o Trello.

Indicamos também a nossa Formação de Produtividade da Alura, na qual você também encontra materiais e cursos sobre outros tipos de ferramentas de organização e gestão de produtos.

Estou muito feliz que você tenha chegado até aqui. Te convido a participar da nossa comunidade no Discord para aprendermos e crescermos juntos! Espero que curta os próximos passos da sua jornada e até a próxima.

Agradecimentos Especiais
Iasmin Araújo, Jhoisnáyra Vitória, Emerson Laranja e Marcus Almeida pelas trocas de ideias, sugestões de melhorias e grande apoio prestado durante a escrita deste artigo.
"""

def analisa_frequencia(texto):
  texto = Counter(texto.lower())
  total_caracteres = sum(texto.values())
  proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in texto.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print(f"{caractere} --> {(proporcao * 100):.2f}%")

analisa_frequencia(texto1)
print("-----------------------")
analisa_frequencia(texto2)
print("-----------------------")