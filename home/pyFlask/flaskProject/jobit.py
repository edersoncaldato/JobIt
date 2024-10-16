from flask import Flask, render_template
app = Flask(__name__)

class Vaga:
  def __init__(self, empresa, tituloVaga, categoriaVaga, requerimentos, descricaoVaga,descricaoCompletaVaga, linkVaga):
    self.empresa=empresa
    self.tituloVaga=tituloVaga
    self.categoriaVaga=categoriaVaga
    self.requisitos=requerimentos
    self.descricaoVaga=descricaoVaga
    self.descricaoCompletaVaga=descricaoCompletaVaga
    self.linkVaga=linkVaga

vaga1 = Vaga('Soft', 'Engenheiro','Engenheiro','Junior','Texto da descrição da vaga', '<ul> <li>Salário competitivo e bônus por desempenho.</li> <li>Plano de saúde e aposentadoria.</li> <li>Horários de trabalho flexíveis e opções de trabalho remoto.</li> <li>Oportunidades de crescimento e desenvolvimento profissional.</li> </ul>', 'vaga')
vaga2 = Vaga('Soft', 'Engenheiro','Engenheiro','Junior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')
vaga3 = Vaga('Soft', 'Engenheiro','Engenheiro','Junior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')
vaga4 = Vaga('Soft', 'Engenheiro','Engenheiro','Junior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')
vaga5 = Vaga('Soft', 'Engenheiro','Engenheiro','Junior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')

vagas = [vaga1, vaga2, vaga3, vaga4, vaga5]
@app.route('/inicio')
def vagaFeed():
  return render_template('source/home.html', vagas=vagas)# trecho da app

@app.route('/vaga')
def vaga():
  return render_template('source/vaga.html', vagas=vagas)

app.run(host='0.0.0.0', port=8080)
