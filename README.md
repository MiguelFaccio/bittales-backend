# BITTALES [BACKEND]

## Requisitos

### Requisitos Funcionais

    1- **Jogos Seguros e Apropriados:**
 
    - Todos os jogos devem ser revisados e classificados de acordo com a faixa etária apropriada.
 
2- **Pesquisa e Filtragem:**
 
    - Sistema de busca avançada que permite aos usuários pesquisar jogos por nome.
    - Filtros de pesquisa dinâmicos que atualizam os resultados em tempo real.
 
3- **Visualização de Pontuações:**
 
    - Painel de pontuação que exibe as pontuações dos jogadores em tempo real.
    - Histórico de pontuações e rankings dos jogadores.
 
 
4- **Compatibilidade Multi-Plataforma:**
 
    - Versões para desktop e dispositivos móveis.
    - Jogos adaptados, se não for possivel adaptação, fazer jogos diferentes.
    - Sistema de Rank único para jogadores mobile.
    - Manter a identidade visual padrão em todos os dispositivos.
 
6- **Administração:**
    
    - Painel administrativo para adicionar, remover e gerenciar usuários.
    - Painel administrativo para adicionar, remover e gerenciar jogos.
    - Sistema de monitoramento de uso e desempenho dos jogos.
    - Sistema de monitoramento de usuários.


### Requisitos Não Funcionais

1- **Segurança:**
 
    - Criptografia de dados sensíveis, como informações de login.
    - Implementação de autenticação de dois fatores para contas de usuário.
 
2- **Desempenho:**
    
    - Evitar ao maximo bugs e uma visão poluida
    - Verficar sempre após updates se há erros.
 
3- **Escalabilidade:**
 
    - Arquitetura do sistema deve permitir fácil adição de novos jogos e funcionalidades.
 
4- **Usabilidade:**
 
    - Interface de usuário deve ser intuitiva e fácil de navegar.
    - Feedback dos usuários deve ser coletado regularmente para melhorias contínuas.
 
5- **Confiabilidade:**
 
    - Backups regulares de dados devem ser realizados para evitar perda de informações.


## Tarefas

- [ ] Implementar o endpoint para a criação de novos usuários.
- [ ] Implementar o endpoint para a criação de novos jogos.
- [ ] Implementar o endpoint para a atualizar os usuários.
- [ ] Implementar o endpoint para a atualizar os jogos.
- [ ] Implementar o endpoint para a remover os usuários.
- [ ] Implementar o endpoint para a remover os jogos.

- [ ] Implementar averificação de usuário para acesso ao endpoint.

- [ ] Limitar o acesso ao endpoint de criar usuários apenas ao perfil admin.
- [ ] Limitar o acesso ao endpoint de criar jogos apenas ao perfil admin.
- [ ] Limitar o acesso ao endpoint de atualizar usuários apenas ao perfil admin.
- [ ] Limitar o acesso ao endpoint de atualizar jogos apenas ao perfil admin.
- [ ] Limitar o acesso ao endpoint de remover usuários apenas ao perfil admin.
- [ ] Limitar o acesso ao endpoint de remover jogos apenas ao perfil admin.