const perguntas = [
{
enunciado:
"Chapeuzinho Vermelho caminhava pela floresta carregando uma cesta para sua avó. De repente, encontrou o lobo. Ele perguntou para onde ela estava indo. O que ela decidiu fazer?",

    alternativas: [
        {
            texto: "🗣️ Contar para onde está indo",

            afirmacao: [
                "Chapeuzinho contou seus planos para um desconhecido.",
                "Ela percebeu depois que não deveria compartilhar informações pessoais com estranhos."
            ]
        },

        {
            texto: "🚶 Ignorar o lobo e continuar",

            afirmacao: [
                "Chapeuzinho decidiu não conversar com um desconhecido.",
                "Ela continuou seu caminho com cuidado.",
                "Ela percebeu que pensar antes de tomar uma decisão pode evitar problemas."
            ]
        }
    ]
},

{
    enunciado:
        "O lobo tentou descobrir onde ficava a casa da avó de Chapeuzinho. O que ela deveria fazer?",

    alternativas: [
        {
            texto: "🏡 Contar onde fica a casa",

            afirmacao: [
                "Chapeuzinho revelou informações sobre sua família.",
                "Ela percebeu que algumas informações pessoais devem ser mantidas em segurança."
            ]
        },

        {
            texto: "🤫 Não contar",

            afirmacao: [
                "Chapeuzinho decidiu proteger as informações sobre sua família.",
                "Ela entendeu que não é seguro contar tudo para pessoas desconhecidas.",
                "Ela demonstrou cuidado ao pensar antes de responder."
            ]
        }
    ]
},

{
    enunciado:
        "Chapeuzinho chegou a uma parte da floresta onde havia dois caminhos. Qual caminho ela deveria escolher?",

    alternativas: [
        {
            texto: "🌲 Escolher o caminho mais seguro",

            afirmacao: [
                "Chapeuzinho preferiu escolher o caminho mais seguro.",
                "Ela pensou nas consequências antes de tomar sua decisão.",
                "Ela mostrou que ter cuidado pode ser importante durante uma aventura."
            ]
        },

        {
            texto: "🐺 Seguir o caminho indicado pelo lobo",

            afirmacao: [
                "Chapeuzinho confiou em uma pessoa que não conhecia.",
                "Ela percebeu que seguir conselhos de desconhecidos pode ser perigoso."
            ]
        }
    ]
}


];

// Controle da aventura

let perguntaAtual = 0;
let coragem = 3;

// Elementos da página

const textoPergunta = document.querySelector("#textoPergunta");
const tituloPergunta = document.querySelector("#tituloPergunta");
const caixaAlternativas = document.querySelector("#alternativas");
const caixaResultado = document.querySelector("#resultado");
const textoCoragem = document.querySelector("#coragem");
const barra = document.querySelector("#barra");

// Mostrar pergunta

function mostrarPergunta() {

const pergunta = perguntas[perguntaAtual];

textoPergunta.textContent = pergunta.enunciado;

tituloPergunta.textContent =
    "Aventura " + (perguntaAtual + 1);

caixaAlternativas.innerHTML = "";

caixaResultado.style.display = "none";

pergunta.alternativas.forEach((alternativa, indice) => {

    const botao = document.createElement("button");

    botao.classList.add("escolha");

    botao.textContent = alternativa.texto;

    botao.addEventListener("click", function () {
        escolher(indice);
    });

    caixaAlternativas.appendChild(botao);
});

atualizarProgresso();


}

// Escolher alternativa

function escolher(indice) {

const pergunta = perguntas[perguntaAtual];

const alternativaEscolhida =
    pergunta.alternativas[indice];

// Se escolher uma alternativa relacionada ao lobo,
// perde um ponto de coragem.

if (indice === 0) {
    coragem--;

    if (coragem < 0) {
        coragem = 0;
    }
}

textoCoragem.textContent = coragem;

mostrarAfirmações(
    alternativaEscolhida.afirmacao
);

// Desativa os botões depois da escolha

const botoes =
    document.querySelectorAll(".escolha");

botoes.forEach(botao => {
    botao.disabled = true;
    botao.style.opacity = "0.6";
    botao.style.cursor = "not-allowed";
});


}

// Mostrar as afirmações

function mostrarAfirmações(afirmacoes) {

caixaResultado.innerHTML = "";

const titulo = document.createElement("strong");

titulo.textContent = "🌟 O que aconteceu?";

caixaResultado.appendChild(titulo);

afirmacoes.forEach(afirmacao => {

    const paragrafo = document.createElement("p");

    paragrafo.textContent = "• " + afirmacao;

    paragrafo.style.marginTop = "10px";

    caixaResultado.appendChild(paragrafo);
});


// Verifica se ainda existem perguntas

if (perguntaAtual < perguntas.length - 1) {

    const botao = document.createElement("button");

    botao.classList.add("proxima");

    botao.textContent = "🌲 Continuar aventura";

    botao.addEventListener("click", proximaPergunta);

    caixaResultado.appendChild(botao);

} else {

    const botao = document.createElement("button");

    botao.classList.add("proxima");

    botao.textContent = "🏡 Chegar à casa da vovó";

    botao.addEventListener("click", finalizar);

    caixaResultado.appendChild(botao);
}

caixaResultado.style.display = "block";


}

// Próxima pergunta

function proximaPergunta() {

perguntaAtual++;

mostrarPergunta();


}

// Final da aventura

function finalizar() {

window.location.href = "final.html";


}

// Atualizar barra de progresso

function atualizarProgresso() {

const progresso =
    ((perguntaAtual + 1) / perguntas.length) * 100;

barra.style.width = progresso + "%";


}

// Começar o jogo

mostrarPergunta();