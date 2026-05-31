# orcamento_aluguel
Este código em Python tem como objetivo gerar um orçamento de aluguel de imóveis de forma automática. Inicialmente, o programa define o valor fixo do contrato em R$ 2.000,00 e solicita ao usuário o tipo de imóvel desejado: apartamento, casa ou estúdio. Caso seja informado um tipo inválido, a execução é encerrada.

Após a escolha do imóvel, o sistema calcula o valor do aluguel com base nas características informadas. Para apartamentos, o valor inicial é de R$ 700,00, podendo aumentar conforme a quantidade de quartos e a inclusão de garagem. Além disso, caso o usuário não possua crianças, é aplicado um desconto de 5% sobre o valor final. Para casas, o valor base é de R$ 900,00, com acréscimos para dois quartos e garagem. Já para estúdios, o valor inicial é de R$ 1.200,00 e pode aumentar de acordo com a quantidade de vagas informadas.

Em seguida, o programa solicita a quantidade de parcelas para o pagamento do contrato, permitindo de uma a cinco parcelas. O valor do contrato é dividido igualmente pelo número de parcelas escolhido. Se o usuário informar uma quantidade inválida, a execução também é interrompida.

Depois dos cálculos, o sistema exibe um resumo do orçamento contendo o valor do aluguel mensal, o valor total do contrato e o valor de cada parcela. Por fim, o usuário pode optar pela geração de um arquivo CSV. Caso escolha essa opção, o programa cria o arquivo “orcamento.csv”, contendo uma tabela com os 12 meses do ano, o valor do aluguel e a parcela do contrato correspondente a cada mês. Após a criação do arquivo, uma mensagem de confirmação é exibida.

Dessa forma, o código automatiza o cálculo de aluguel, parcelamento de contrato e geração de relatórios, facilitando a organização e o controle financeiro das locações.
