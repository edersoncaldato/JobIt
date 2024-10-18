from flask import Flask, render_template
app = Flask(__name__)

class Vaga:
  def __init__(self, id, empresa, tituloVaga, categoriaVaga, requerimentos, descricaoVaga,descricaoCompletaVaga, linkVaga):
    self.id = id
    self.empresa=empresa
    self.tituloVaga=tituloVaga
    self.categoriaVaga=categoriaVaga
    self.requisitos=requerimentos
    self.descricaoVaga=descricaoVaga
    self.descricaoCompletaVaga=descricaoCompletaVaga
    self.linkVaga=linkVaga
#
# class textoVaga:
#   def __init__(self, corpoVaga, vagaSalario, ):

vaga1 = Vaga('0','Soft', 'Engenheiro','Engenheiro','Junior','Texto da descrição da vaga', '<ul> <li>Salário competitivo e bônus por desempenho.</li> <li>Plano de saúde e aposentadoria.</li> <li>Horários de trabalho flexíveis e opções de trabalho remoto.</li> <li>Oportunidades de crescimento e desenvolvimento profissional.</li> </ul>', 'vaga')
vaga2 = Vaga('1','Soft', 'Cabalei','Engenheiro','Junior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')
vaga3 = Vaga('2','Soft', 'FDJFDSF','Engenheiro','Junior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')
vaga4 = Vaga('3','Soft', 'DIFERENTE','Engenheiro','Junior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')
vaga5 = Vaga('4','Soft', 'AAA','Engenheiro','Jun ior','Texto da descrição da vaga', 'Principais Responsabilidades: Desenvolver designs e arquiteturas de software de alta qualidade. Escrever código limpo e escalável usando as linguagens .NET e C#. Colaborar com equipes multifuncionais para definir e entregar novas funcionalidades. Solucionar problemas, depurar e atualizar software existente. Requisitos: Graduação em Ciência da Computação ou área relacionada. Experiência comprovada como Engenheiro de Software ou função semelhante. Experiência em design e desenvolvimento de software em um ambiente orientado a testes. Proficiência no framework .NET e na linguagem de programação C#. Benefícios: Salário competitivo e bônus por desempenho. Plano de saúde e aposentadoria. Horários de trabalho flexíveis e opções de trabalho remoto. Oportunidades de crescimento e desenvolvimento profissional.', 'vaga')

vagas = [vaga1, vaga2, vaga3, vaga4, vaga5]
@app.route('/inicio')
def vagaFeed():
  return render_template('source/home.html', vagas=vagas)# trecho da app

@app.route('/vaga/<int:vaga_id>')
def vaga(vaga_id):
    # Verificar se a lista de vagas está vazia
    if not vagas:
        return 'Não há vagas disponíveis no momento', 404

    # Encontrar a vaga com o ID correspondente
    vaga = next((v for v in vagas if v.id == str(vaga_id)), None)  # Converter vaga_id para string para comparação

    if vaga:
        return render_template('source/vaga.html', vaga=vaga)
    else:
        return 'Vaga não encontrada', 404


@app.route('/login')
def login():
  return render_template('source/login.html')

@app.route('/registro')
def registro():
  return render_template('source/register.html')

@app.route('/profile')
def profile():
  return render_template('source/profile.html')

@app.route('/help')
def help():
  return render_template('source/help.html')

app.run(host='0.0.0.0', port=8080)
