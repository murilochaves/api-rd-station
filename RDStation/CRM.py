import json  # estrutura de dados
import Modulos.RDStation.Erros as excessoes  # erros
import pandas as pd  # estrutura de dados
import requests  # requisições http
import time  # tempo de delay


# classe de conexão com o api do rdstation
class APIRDStationCRM(object):

    # - # - #   Construtor   # - # - #

    def __init__(self, token, printar=False) -> None:

        # token de conexão com o api do rdstation
        self.token = token

        # variáveis auxiliares
        self.cabecalho = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.delay = .5  # tempo de delay entre as requisições (120 por minuto, 2 por segundo, 0.5 entre as requisições)
        self.endpoint_autenticacao = 'auth/dialog?'
        self.url = 'https://crm.rdstation.com/api/v1/'

        # se for para printar
        if printar:

            # exibindo o token
            print(f'> Token da API: {self.token[:3]}...{self.token[-3:]}')

    # - # - #   Token de Autenticação   # - # - #

    def exibir_token(self) -> json:
        return self.get('token/check')
    
    # - # - #   Contatos   # - # - #

    def listar_contatos(
            self,  # Token do usuário
            page=None,  # Número atual da página
            limit=20,  # Limite de contatos que serão listados. Valor padrão é 20. Valor máximo é 200
            order='name',  # Campo a ser ordenado. Valor padrão é "name"
            direction='asc',  # Ordenação da lista. "asc" ou "desc", padrão é "asc"
            email=None,  # Filtra os resultados pelo e-mail informado
            q=None,  # Nome do contato a ser buscado
            phone=None,  # Filtra os resultados pelo telefone informado
            title=None,  # Filtra os resultados pelo cargo informado
        ) -> json:
 
        # parametros
        parametros = {
            'page': page,
            'limit': limit,
            'order': order,
            'direction': direction,
            'email': email,
            'q': q,
            'phone': phone,
            'title': title
        }
        
        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('contacts', parametros=parametros)

        return retorno

    def exibir_contato(self, contact_id) -> json:
        return self.get(f'contacts/{contact_id}')

    # def criar_contato():
    #     pass

    # def atualizar_contato():
    #     pass

    # - # - #   Empresas   # - # - #

    def listar_empresas(
            self,  # Token do usuário
            page=None,  # Número atual da página
            limit=20,  # Limite de contatos que serão listados. Valor padrão é 20. Valor máximo é 200
            order='name',  # Campo a ser ordenado. Valor padrão é "name"
            direction='asc',  # Ordenação da lista. "asc" ou "desc", padrão é "asc"
            organization_segment=None,  # ID do segmento. Busca todas as empresas que têm esse segmento
            user_id=None,  # ID do usuário. Busca todas as empresas que têm esse usuário
            q=None  # String com o nome da empresa. Busca as empresas com a string anterior no parâmetro
        ):

        # parametros
        parametros = {
            'page': page,
            'limit': limit,
            'order': order,
            'direction': direction,
            'organization_segment': organization_segment,
            'user_id': user_id,
            'q': q
        }
        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('organizations', parametros=parametros)

        return retorno
    
    def exibir_empresa(self, organization_id) -> json:
        return self.get(f'organizations/{organization_id}')
    
    # def criar_empresa():
    #     pass

    # def atualizar_empresa():
    #     pass

    def listar_contatos_empresa(
            self,  # Token do usuário
            organization_id,  # ID da empresa
            page=None,  # Número atual da página
            limit=20,  # Limite de contatos que serão listados. Valor padrão é 20. Valor máximo é 200
        ) -> json:

        # parametros
        parametros = {
            'organization_id': organization_id,
            'page': page,
            'limit': limit
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get(f'organizations/{organization_id}/contacts', parametros=parametros)

        return retorno

    # - # - #   Negociações   # - # - #

    def listar_negociacoes(
        self,  # Token do usuário
        page=1,  # Número atual da página
        limit=20,  # Limite de negociações que serão listadas. Valor padrão é 20. Valor máximo é 200
        order='created_at',  # Ordenação. Valor padrão é "created_at"
        direction='desc',  # Ordenação da lista. "asc" ou "desc", padrão é "desc"
        name=None,  # Nome da negociação. Para buscas com nome exato, usar o parâmetro exact_name= true
        win=None,  # Negociações ganhas. O valor true (retorna as negociações "ganhas"), false (retorna as negociações "perdidas") e null (retorna as negociações "em aberto")
        user_id=None,  # ID do usuário relacionado à negociação
        closed_at=None,  # Ao informar true (retorna as negociações "ganhas" ou "perdidas"). Ao informar false (retorna as negociações "em aberto" OU "pausadas")
        closed_at_period=None,  # Data de fechamento da negociação: se true deve ser informado start_date e end_date
        created_at_period=None,  # Data de criação da negociação: se true, deve ser informado start_date e end_date
        prediction_date_period=None,  # Data de previsão de fechamento da negociação: se true, deve ser informado start_date e end_date
        start_date=None,  # Primeiro dia/hora em que deve ser aplicado o filtro para o parâmetro closed_at_period ou created_at_period. Ex.: "start_date": "2020-12-14T15:00:00"
        end_date=None,  # Último dia/hora em que deve ser aplicado o filtro para o parâmetro closed_at_period ou created_at_period. Ex.: "end_date": "2020-12-14T15:00:00"
        campaign_id=None,  # ID da campanha
        deal_stage_id=None,  # ID da etapa
        deal_lost_reason_id=None,  # ID do motivo de perda
        deal_pipeline_id=None,  # ID do funil
        organization=None,  # ID da empresa
        hold=None,  # Estado da negociação pausada. Se marcado como true (retorna todas negociações "pausadas"). Para outros casos, não deve-se utilizar esse parâmetro
        product_presence=None,  # Negociações que contenham produtos/serviços relacionados. Se false (nenhum produto relacionado), true (um ou mais produtos relacionados) ou uma lista de IDs de produto. A lista de IDs deve ser informada com os valores separados por vírgula. Ex.: 5esdsds, d767dsdssd, c6e40fd2f000972a083
        next_page=None,  # O parâmetro next_page serve para consultar a próxima página de resultados da busca corrente. Ele é obtido através da primeira consulta feita por esta API, porém todos os demais resultados apresentam este campo que se utilizado na requisição, navegam para sua próxima página.
    ) -> json:
        
        # se não informado a data final
        if not end_date:

            # atribuindo a data de início
            end_date = start_date
        
        # se for informado as datas 
        if (start_date == True) and ('t' not in str(start_date).lower()):
            start_date = f'{start_date}T00:00:00'
        
        if (end_date == True) and ('t' not in str(end_date).lower()):
            end_date = f'{end_date}T23:59:59'
        
        # parametros
        parametros = {
            'page': page,
            'limit': limit,
            'order': order,
            'direction': direction,
            'name': name,
            'win': win,
            'user_id': user_id,
            'closed_at': closed_at,
            'closed_at_period': closed_at_period,
            'created_at_period': created_at_period,
            'prediction_date_period': prediction_date_period,
            'start_date': start_date,
            'end_date': end_date,
            'campaign_id': campaign_id,
            'deal_stage_id': deal_stage_id,
            'deal_lost_reason_id': deal_lost_reason_id,
            'deal_pipeline_id': deal_pipeline_id,
            'organization': organization,
            'hold': hold,
            'product_presence': product_presence,
            'next_page': next_page
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('deals', parametros=parametros)

        return retorno
       
    def exibir_negociacao(self, deal_id) -> json:
        return self.get(f'deals/{deal_id}')

    # def criar_negociacao():
    #     pass

    # def atualizar_negociacao():
    #     pass

    def listar_contatos_da_negociacao(
            self,  # Token do usuário
            deal_id,  # ID da negociação
            page=1,  # Página da listagem de contatos da negociação. Valor padrão é 1
            limit=20  # Limite de contatos que virão por listagem. Valor padrão é 20. Valor máximo é 200
        ) -> json:

        # parametros
        parametros = {
            'deal_id': deal_id,
            'page': page,
            'limit': limit
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get(f'deals/{deal_id}/contacts', parametros=parametros)

        return retorno

    def listar_interacoes_lead(
        self, 
        lead_id,  # ID do lead
        page=None,  # Número atual da página
        limit=20,  # Limite de interações que serão listadas. Valor padrão é 20. Valor máximo é 200
        order='date',  # Campo a ser ordenado. Valor padrão é "date"
        direction='asc',  # Ordenação da lista. "asc" ou "desc", padrão é "asc"
        type=None,  # Filtra os resultados pelo tipo de interação
        start_date=None,  # Filtra os resultados pela data de início
        end_date=None  # Filtra os resultados pela data de fim
    ) -> json:

        # parametros
        parametros = {
            'lead_id': lead_id,
            'page': page,
            'limit': limit,
            'order': order,
            'direction': direction,
            'type': type,
            'start_date': start_date,
            'end_date': end_date,
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get(f'leads/{lead_id}/interactions', parametros=parametros)

        return retorno
    
    def listar_data_primeira_negociacao(self) -> str:

        # pegando a primeira negociacao
        negociacao = self.listar_negociacoes(
            limit=1, order='created_at', direction='asc'
        )

        # pegando a data da primeira negociacao
        data = negociacao['deals'][0]['created_at']

        # convertendo para o formato de data YYYY-MM-DD
        data = pd.to_datetime(data).strftime('%Y-%m-%d')

        return data
    
    def listar_ids(self, inicio, fim=None, delay=False, limit=200, printar=False) -> list:

        # se não for informado uma data final
        if not fim:

            # processando apenas uma respectiva data
            fim = inicio

        # variáveis auxiliares
        pagina, ids = 1, []

        # enquanto houver ids para coletar
        while True:

            # realizando requisicao
            dados = self.listar_negociacoes(
                page=pagina,
                created_at_period=True, start_date=inicio, end_date=fim
            )

            # extraindo todos os ids
            novos_ids = [deal['id'] for deal in dados.get('deals', [])]
            
            # adicionando os ids na lista+
            ids.extend(novos_ids)

            # se não houver mais ids para coletar, interrompe o loop
            if not novos_ids:
                break

            # incrementando a página (contador)
            pagina += 1

            # se for para haver um delay
            if delay:

                # aguarda um tempo
                time.sleep(self.delay)

        # se for para printar
        if printar:

            # exibindo os ids
            print(f'\t> {len(ids)} IDs coletados: [{ids[0]}, ..., {ids[-1]}]')

        return ids
    
    def listar_todas_negociacoes(self, inicio, fim=None, delay=False, limit=200, printar=False) -> list:

        # se não for informado uma data final
        if not fim:

            # processando apenas uma respectiva data
            fim = inicio

        # variáveis auxiliares
        pagina, negociacoes = 1, []

        # enquanto houver ids para coletar
        while True:

            # coletando a primeira página 
            if pagina == 1:

                # realizando requisicao
                dados = self.listar_negociacoes(
                    page=pagina, limit=limit,
                    created_at_period=True, start_date=inicio, end_date=fim
                )

            # realizando chamada pela next_page
            else:
                dados = self.listar_negociacoes(
                    limit=limit,
                    created_at_period=True, start_date=inicio, end_date=fim,
                    next_page=proxima_pagina
                )

            # extraindo todos os ids
            novas_negociacoes = [deal for deal in dados.get('deals', [])]
            
            # adicionando os ids na lista+
            negociacoes.extend(novas_negociacoes)

            # próxima página
            proxima_pagina = dados.get('next_page', False)

            # incrementando a página (contador)
            pagina += 1

            # se não houver mais ids para coletar, interrompe o loop
            if (not novas_negociacoes) or (not proxima_pagina):
                break

            # se for para haver um delay
            if delay:

                # aguarda um tempo
                time.sleep(self.delay)

        return negociacoes

    def contar_negociacoes(self, data, printar=False) -> int:
        '''
        retorna a quantidade de negociações de um respectivo dia
        '''

        # realizando a requisição
        retorno = self.listar_negociacoes(limit=1, created_at_period=True, start_date=data, end_date=data)

        # contando as negociações
        total = retorno.get('total', 0)

        # se for para printar
        if printar:

            # exibindo a quantidade de negociações
            print(f'> {total} negociações')

        return total

    # - # - #   Produtos nas Negociações   # - # - #

    def listar_produtos_negociacao(
            self,  # Token do usuário
            deal_id  # ID da negociação
        ) -> json:

        # realizando a requisição
        retorno = self.get(f'deals/{deal_id}/deal_products')

        return retorno

    # def criar_produto_em_negociacao():
    #     pass

    # def criar_produtos_em_massa_em_negociacao():
    #     pass

    # def atualizar_produto_em_negociacao():
    #     pass

    # def atualizar_produtos_em_massa_em_negociacao():
    #     pass

    # def deletar_produto_em_negociacao():
    #     pass

    # def deletar_produtos_em_massa_em_negociacao():
    #     pass

    # - # - #   Produtos   # - # - #

    def listar_produtos(
        self,  # Token do usuário
        page=1,  # Número atual da página
        limit=20,  # Limite de produtos que serão listados. Valor padrão é 20. Valor máximo é 200 
    ):
        
        # parametros
        parametros = {
            'page': page,
            'limit': limit
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('products', parametros=parametros)

        return retorno

    def exibir_produto(self, product_id) -> json:
        return self.get(f'products/{product_id}')
    
    # def criar_produto():
    #     pass

    # def atualizar_produto():
    #     pass

    # - # - #   Campos personalizados   # - # - #

    def listar_campos_personalizados(
        self,  # Token do usuário
        _for=None  # Seleciona os campos personalizados da entidade fornecida. Os valores permitidos são: deal, contact e organization
    ) -> json:
        
        # parametros
        parametros = {
            'for': _for
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('custom_fields', parametros=parametros)

        return retorno

    def exibir_campo_personalizado(self, custom_field_id) -> json:
        return self.get(f'custom_fields/{custom_field_id}')

    # def criar_campo_personalizado():
    #     pass

    # def atualizar_campo_personalizado():
    #     pass

    # def deletar_campo_personalizado():
    #     pass

    # - # - #   Funil de Venda   # - # - #

    def listar_funil_de_venda(
        self,  # Token do usuário
        limit=20,  # Limite de funis de vendas que virão por listagem. Valor padrão é 20. Valor máximo é 200
        page=1  # Página da listagem de funis de vendas. Valor padrão é 1
    ) -> json:
        
        # parametros
        parametros = {
            'limit': limit,
            'page': page
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('deal_pipelines', parametros=parametros)

        return retorno

    def exibir_funil_de_venda(self, deal_pipeline_id) -> json:
        return self.get(f'deal_pipelines/{deal_pipeline_id}')
    
    # def criar_funil_de_venda():
    #     pass

    # def atualizar_funil_de_venda():
    #     pass

    # - # - #   Etapas do Funil de Vendas   # - # - #

    def listar_etapas_do_funil_de_vendas(
        self,  # Token do usuário
        deal_pipeline_id=None,  # ID do Funil de Vendas. Caso o parâmetro não seja passado ou não existe um funil de vendas do ID especificado, será retornada as etapas do funil de vendas padrão
        limit=12,  # Limite de etapas do funil de vendas que virão por listagem. Valor padrão é 12. Valor máximo é 12
        page=None  # Página da listagem de etapas do funil de venda
    ) -> json:
        
        # parametros
        parametros = {
            'deal_pipeline_id': deal_pipeline_id,
            'limit': limit,
            'page': page
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('deal_stages', parametros=parametros)

        return retorno
    
    def exibir_etapa_do_funil_de_vendas(self, deal_stage_id) -> json:
        return self.get(f'deal_stages/{deal_stage_id}')
    
    # def criar_etapa_do_funil_de_vendas():
    #     pass

    # def atualizar_etapa_do_funil_de_vendas():
    #     pass

    # - # - #   Tarefas   # - # - #

    def listar_tarefas(
        self,  # Token do usuário
        page=1,  # Número da página listada. Valor padrão é 1
        limit=20,  # Limite de tarefas que virão por listagem. Valor padrão é 20. Valor máximo é 200
        deal_id=None,  # ID da negociação
        done=None,  # Se a tarefa está concluída
        type=None,  # Tipo de tarefa. Valores possíveis: (call, email, meeting, task, lunch, visit, whatsapp)
        user_id=None,  # ID do usuário
        date_start=None,  # Filtrar por data de início
        date_end=None,  # Filtrar por data final
        done_date_start=None,  # Filtrar por data de conclusão - início
        done_date_end=None,  # Filtrar por data de conclusão - final
    ) -> json:
        
        # parametros
        parametros = {
            'page': page,
            'limit': limit,
            'deal_id': deal_id,
            'done': done,
            'type': type,
            'user_id': user_id,
            'date_start': date_start,
            'date_end': date_end,
            'done_date_start': done_date_start,
            'done_date_end': done_date_end
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('tasks', parametros=parametros)

        return retorno

    def exibir_tarefa(self, task_id) -> json:
        return self.get(f'tasks/{task_id}')
    
    # def criar_tarefa():
    #     pass

    # def atualizar_tarefa():
    #     pass

    # - # - #   Anotações   # - # - #

    def listar_anotacoes(
            self,  # Token do usuário
            deal_id=None,  # ID da negociação
            page=1,  # Número da página listada. Valor padrão é 1
            limit=20,  # Limite de anotações que virão por listagem. Valor padrão é 20. Valor máximo é 200
            start_date=None,  # Filtrar por data - início
            end_date=None,  # Filtrar por data - fim
    ) -> json:
        
        # parametros
        parametros = {
            'deal_id': deal_id,
            'page': page,
            'limit': limit,
            'start_date': start_date,
            'end_date': end_date
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('activities', parametros=parametros)

        # verificando se, existem outras páginas
        if retorno['has_more'] == True and retorno['next_page'] != None:
            pass

        return retorno

    # def exibir_anotacao():
    #     pass

    # - # - #   Usuários   # - # - #

    def listar_usuarios(
        self,  # Token do usuário
        active=None,  # Se o usuário está ativo
    ) -> json:
        
        # parametros
        parametros = {
            'active': active
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('users', parametros=parametros)

        return retorno
    
    def exibir_usuario(self, user_id) -> json:
        return self.get(f'users/{user_id}')

    # - # - #   Equipes   # - # - #

    def listar_equipes(self):
        return self.get('teams')

    def exibir_equipe(self, team_id) -> json:
        return self.get(f'teams/{team_id}')

    # - # - #   Fontes   # - # - #

    def listar_fontes(
            self,  # Token do usuário
            limit=20,  # Limite de fontes que virão por listagem. Valor padrão é 20. Valor máximo é 200 
            page=1,  # Número atual da página. Valor padrão é 1
            q=None  # Nome da fonte a ser buscada. Ex: a fonte "Facebook Ads" deve ser buscada como "facebook%20ads"
        ):

        # parametros
        parametros = {
            'limit': limit,
            'page': page,
            'q': q
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('deal_sources', parametros=parametros)

        return retorno

    def exibir_fonte(self, deal_source_id) -> json:
        return self.get(f'deal_sources/{deal_source_id}')
    
    # def criar_fonte():
    #     pass

    # def atualizar_fonte():
    #     pass

    # - # - #   Campanhas   # - # - #

    def listar_campanhas(
            self,  # Token do usuário
            limit=20,  # Limite de campanhas que virão por listagem. Valor padrão é 20. Valor máximo é 200
            page=1,  # Número atual da página. Valor padrão é 1
            q=None  # Nome da campanha a ser buscada. Ex: a campanha "Facebook Ads" deve ser buscada como "facebook%20ads"
        ) -> json:

        # parametros
        parametros = {
            'limit': limit,
            'page': page,
            'q': q
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('campaigns', parametros=parametros)

        return retorno
    
    def exibir_campanha(self, campaign_id) -> json:
        return self.get(f'campaigns/{campaign_id}')
    
    # def criar_campanha():
    #     pass

    # def atualizar_campanha():
    #     pass

    # - # - #   Motivos de Perda   # - # - #

    def listar_motivos_de_perda(
            self,  # Token do usuário
            limit=20,  # Limite de motivos da perda que virão por listagem. Valor padrão é 20. Valor máximo é 200
            page=1,  # Página da listagem de motivos da perda. Valor padrão é 1
            q=None,  # Nome do motivo da perda a ser buscado. Ex: a fonte "Motivo 1" deve ser buscada como "motivo%201"
            order='name',  # Campo a ser ordenado. Valor padrão e aceito é "name"
    ) -> json:
        
        # parametros
        parametros = {
            'limit': limit,
            'page': page,
            'q': q,
            'order': order
        }

        # remove parametros sem uso
        parametros = {
            chave: valor for chave, valor in parametros.items() if valor is not None
        }

        # realizando a requisição
        retorno = self.get('deal_lost_reasons', parametros=parametros)

        return retorno

    def exibir_motivo_de_perda(self, deal_lost_reason_id) -> json:
        return self.get(f'deal_lost_reasons/{deal_lost_reason_id}')

    # def criar_motivo_de_perda():
    #    pass

    # def atualizar_motivo_de_perda():
    #   pass
    
    # - # - #   Webhooks   # - # - #    

    def listar_webhooks(self):
        return self.get('webhooks')
    
    # def criar_webhook():
    #     pass

    def exibir_webhook(self, uuid) -> json:
        return self.get(f'webhooks/{uuid}')

    # def atualizar_webhook():
    #     pass

    # def deletar_webhook():
    #     pass
    
    # - # - #   Funções Auxiliares   # - # - #

    def get(self, endpoint, **kwargs):

        # realizando a requisição
        retorno = self.request('GET', endpoint, **kwargs)

        # realizando o parse da resposta
        retorno = self.parse(retorno)

        return retorno

    def request(self, method, endpoint, cabecalho=None, parametros={}, **kwargs):

        # adicionando o token ao cabeçalho
        parametros.update(token=self.token)

        # realizando a requisição
        retorno = requests.request(method, self.url + endpoint, headers=self.cabecalho, params=parametros, **kwargs)

        return retorno

    def parse(self, resposta):

        # código de resposta
        codigo = resposta.status_code

        # parse da resposta
        if "Content-Type" in resposta.headers and "application/json" in resposta.headers["Content-Type"]:
            
            try:
                r = resposta.json()
            
            except ValueError:
                r = resposta.text
        
        # resposta sem conteúdo
        else:
            r = resposta.text

        if codigo == 200:
            return r

        # lista de erros
        erros = {
            400: excessoes.BadRequestError,
            401: excessoes.UnauthorizedError,
            404: excessoes.NotFoundError,
            422: excessoes.UnprocessableEntityError,
            429: excessoes.TooManyRequestsError,
            500: excessoes.InternalServerError
        }

        # se houver erro
        if codigo in erros:
            
            # apresenta a exceção correspondente
            raise erros[codigo](r)

        return r
