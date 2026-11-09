# projetoFinal25
# 🚀 Guia Prático de Git e GitHub para as Aulas

Bem-vindo(a)! Este guia prático ensina o passo a passo para criar sua conta no GitHub, fazer o fork do repositório da disciplina, cloná-lo na sua máquina com o VS Code e enviar suas alterações usando commit e push.

---

## 1. Criando sua Conta no GitHub

Se você ainda não possui uma conta no GitHub:

1. Acesse **[github.com](https://github.com)** e clique no botão **Sign up** (canto superior direito).
2. Digite seu e-mail (prefira um e-mail que você acessa com frequência).
3. Crie uma senha forte e escolha um nome de usuário (`username`) amigável e profissional.
4. Complete a verificação de segurança (captcha) e insira o código numérico enviado para seu e-mail.
5. Siga as perguntas iniciais ou clique em pular até chegar ao seu painel inicial.

---

## 2. O que é e Como Fazer um Fork

> **O que é um Fork?**  
> Fazer um *fork* significa criar uma cópia idêntica do repositório do professor diretamente dentro da sua própria conta do GitHub. Assim, você pode alterar códigos e realizar atividades sem modificar o projeto original.

### Passo a passo para o Fork:
1. Copie o link desse repositório e abra no seu navegador.
2. No canto superior direito da página, localize e clique no botão **Fork** (ícone de bifurcação).
3. Na janela que se abrir:
   - Verifique se o **Owner** selecionado é o seu usuário.
   - Deixe o nome do repositório como está (ou ajuste conforme orientações do professor).
   - Mantenha a opção *"Copy the `main` branch only"* marcada.
4. Clique em **Create fork**.
5. Aguarde alguns segundos. Você será redirecionado para a página do repositório agora sob a sua conta (ex: `github.com/seu-usuario/nome-do-repositorio`).

---

## 3. Clonando o Repositório no VS Code

Agora vamos baixar a sua cópia para o computador de trabalho.

1. Na página do **seu fork** no GitHub, clique no botão verde **`<> Code`**.
2. Na aba **HTTPS**, copie a URL exibida (algo como `https://github.com/seu-usuario/nome-do-projeto.git`).
3. Abra o **Visual Studio Code (VS Code)** no seu computador.
4. Pressione as teclas `Ctrl + Shift + P` (no Windows/Linux) ou `Cmd + Shift + P` (no macOS) para abrir a paleta de comandos.
5. Digite `Git: Clone` e pressione **Enter**.
6. Cole a URL copiada no passo 2 e aperte **Enter**.
7. Escolha uma pasta no seu computador onde deseja salvar o projeto (ex: pasta `Projetos` ou `Documentos`).
8. Quando o download terminar, o VS Code exibirá uma notificação no canto inferior direito: clique em **Open** (Abrir) para carregar o projeto.

---

## 4. Configurando sua Identidade no Git (Apenas 1ª vez na máquina)

Se for a primeira vez usando o Git nessa máquina, abra o terminal no VS Code (`Ctrl + '` ou menu **Terminal > New Terminal**) e execute os comandos abaixo substituindo pelos seus dados:

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email-do-github@exemplo.com"
```

---

## 5. Fazendo Alterações e Commits

> **O que é um Commit?**  
> Um *commit* é um ponto de salvamento do histórico do seu projeto. Ele registra o que foi alterado e acompanha uma mensagem explicativa.

### Pelo Terminal do VS Code:
1. Faça as edições nos arquivos ou crie novos arquivos necessários para a atividade.
2. Salve os arquivos modificados (`Ctrl + S`).
3. No terminal do VS Code, verifique o que foi modificado:
   ```bash
   git status
   ```
4. Adicione os arquivos ao palco de envio (*stage*):
   ```bash
   git add .
   ```
5. Registre o commit com uma mensagem descritiva:
   ```bash
   git commit -m "Implementa exercicio 1 da aula de logica"
   ```

*(Opcional - Pela interface visual do VS Code)*:  
Se preferir a interface visual, clique no ícone de **Source Control** (três pontos conectados) na barra lateral esquerda, digite sua mensagem na caixa de texto e clique no botão **Commit** (ou no ícone de check `✓`).

---

## 6. Enviando suas Alterações com Push

> **O que é o Push?**  
> O comando *push* envia os commits salvos no seu computador local para a sua conta remota no GitHub.

1. No terminal do VS Code, execute:
   ```bash
   git push origin main
   ```
   *(Nota: Se o branch principal do seu projeto se chamar `master`, use `git push origin master`)*.
2. Caso seja a primeira vez enviando da máquina, o VS Code abrirá uma janela no navegador pedindo autorização: clique em **Authorize GitCredentialManager** ou faça o login com sua conta do GitHub.
3. Para confirmar que deu certo: volte na página do seu repositório no navegador (`github.com/seu-usuario/...`) e recarregue a página (`F5`). Você verá seus novos arquivos e a mensagem de commit atualizada!

