<!--
PROJETO: BRICKMASTER RAIZ
DOCUMENTO: IFNC ATLAS — Contratos de Integração
IDENTIFICADOR: BM-020-CONTRACTS
VERSÃO: 0.1.0
ESTADO: DOCUMENTADO — EXPERIMENTAL — NÃO VALIDADO
CRIADO EM: 2026-11-02
ÚLTIMA REVISÃO: 2026-11-02
SHA-256: ver CHECKSUMS.sha256 (SHA-256 do conteúdo integral)
COMMIT DE REFERÊNCIA: 4f5b5ad608fd045e6b5d48d8603239264843e719
RESPONSÁVEL: Carlos Andrade
REPOSITÓRIO: https://github.com/carlos-andrade/BRICKMASTER_GERAL
HISTÓRICO:
- 2026-11-02 | v0.1.0 | Contratos de dados e integração inicial.
FONTE DA VERDADE: repositório oficial.
-->

# CONTRACTS — IFNC ATLAS

## 1. Envelope comum

Toda mensagem deve conter:
- schema_version: versão do contrato;
- module_id: BM-020;
- event_id: identificador único;
- event_time_utc: instante econômico do evento;
- ingest_time_utc: instante de captura;
- session_date: data do pregão B3;
- source_id e source_version;
- instrument_id e instrument_type;
- payload;
- quality: status, freshness_ms, completeness, warnings;
- lineage: referência aos dados de origem, transformação, código e parâmetros.

## 2. MarketObservation

Entradas normalizadas:
- instrument_id: IFNC | IBOV | WIN:<contract>.
- price/value: decimal, unidade explícita.
- volume/turnover: opcional, com unidade e semântica da fonte.
- event_time, ingest_time, source_time.
- session_status: PRE_OPEN | AUCTION | CONTINUOUS | CLOSING | CLOSED.
- source_id, source_sequence, revision_id.

Não aceitar preço sem moeda/unidade, timestamp sem timezone ou WIN sem identificação do contrato.

## 3. ConstituentsSnapshot

- effective_from / effective_to;
- published_at / captured_at;
- methodology_version;
- constituent_id / ticker;
- official_weight;
- free_float_factor, quando fornecido;
- source_document_hash;
- correction_of, quando revisão.

Uma carteira só pode ser aplicada a timestamps dentro de sua vigência e após sua disponibilidade pública/operacional registrada.

## 4. QualityReport

- status: OK | DEGRADED | BLOCKED;
- stale: boolean;
- missing_intervals;
- duplicate_count;
- out_of_order_count;
- timestamp_skew_ms;
- expected_count / observed_count;
- constituent_coverage;
- weighted_coverage;
- reasons[].

## 5. AtlasFeatures

- horizon;
- relative_strength;
- divergence;
- breadth;
- weighted_participation;
- dispersion;
- relative_volatility;
- vwap_alignment (nullable);
- constituent_coverage;
- weighted_coverage;
- valid_from / calculated_at;
- feature_version;
- source_event_ids[].

Todos os valores numéricos devem ter unidade e precisão declaradas. Null significa indisponível; nunca substituir por zero.

## 6. AtlasState

- state: FINANCIAL_SECTOR_STRONG | FINANCIAL_SECTOR_WEAK | MIXED | NEUTRAL | DEGRADED | BLOCKED;
- confidence: decimal [0,1], qualidade da evidência e não probabilidade de acerto;
- horizon;
- evidence[]: feature, value, threshold_version, interpretation;
- contradictions[];
- invalidation_conditions[];
- quality_report_id;
- generated_at;
- expires_at;
- model_version.

## 7. GyroscopeContext

O adaptador BM-020 -> BM-001 só publica contexto:
- sector_state;
- sector_confidence;
- horizon;
- evidence_refs[];
- contradictions[];
- data_quality;
- freshness;
- invalidation_conditions;
- source_version.

Não publicar BUY/SELL, ordem, preço, stop, alvo ou sizing. O Giroscópio preserva conflitos com outros módulos; não deve apagar divergência para fabricar consenso.

## 8. Política de falha

- Dado crítico ausente: BLOCKED.
- Atraso acima do limite configurado por fonte/horizonte: DEGRADED.
- Carteira histórica ausente: bloquear features ponderadas; não usar carteira atual.
- Desalinhamento temporal acima do limite: invalidar cálculo combinado.
- Fonte contraditória: marcar conflito; não escolher silenciosamente uma fonte.
- Falha no adaptador: watchdog alerta; nenhum efeito sobre execução.

## 9. Dependências

Obrigatórias:
- BM-018 Dados e Qualidade;
- BM-011 IBOV / Intermercado;
- relógio/sessões B3 e identificação de contratos WIN;
- registro histórico append-only.

Integração:
- BM-001 Giroscópio;
- BM-016 Replay e Backtest;
- BM-017 Watchdog.

Opcionais, conforme disponibilidade:
- dados intradiários de constituintes;
- calendário macroeconômico;
- dados de VWAP, volume e negócios.

## 10. Versionamento

Mudanças incompatíveis elevam major; campos opcionais compatíveis elevam minor; correções sem alteração semântica elevam patch. Consumidores devem rejeitar schema desconhecido em campos críticos e registrar a rejeição.
