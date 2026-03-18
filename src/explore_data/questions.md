# Réponses aux questions partie 1 sur les fichiers du bucket S3

1. How many columns does products.csv have? Which ones start with + (internal columns)?
   => il y a 21 colonnes dont 4 avec un "+ " devant le nom :
   - internal_cost_usd
   - supplier_id
   - warehouse_location
   - internal_cost_code

2. How many columns does users.csv have? Can you spot PII (passwords, IPs)?
   => il y a 28 colonnes dont 8 avec "+ " :
   - hashed_password str
   - ga_client_id str
   - fbp str
   - device_fingerprint str
   - last_ip str
   - failed_login_count int64
   - account_flags int64
   - internal_segment_id int64

   Pour voir les hashed mdp : "print(df["_hashed_password"].unique()) " (bon de base il sont unique les hash à moins que plusieurs fois le meme mdp )
   => ['$2b$12$4cdd64ea06c59f9f0a93434701564a33437050c4ba37340175c52',
 '$2b$12$89ed6c642bf0d24f3f3f4bd1324c5e8a29d8738875f414b50ae08',
 '$2b$12$30b2989c477c6ccbdd4491479c62dce4ce4b9b2f3458b654a7bc0',
 '$2b$12$be0342d0b45a010fee5b58b8b697cd4a1230c404f9ef0259b9564', ....

Pour les ips : "print(df["_last_ip"].unique())"

[ '98.116.213.62', '76.211.210.78', '64.83.98.58', '108.233.21.225',
'76.230.12.46', '64.83.74.46', '162.142.106.13', '73.165.188.230',
'142.181.66.158', '73.153.165.197',

3. In orders.csv, what are the possible values for status?
   => On a ces champs possibles dans le csv :
   ['delivered', 'shipped', 'returned', 'chargeback', 'cancelled', 'processing']

4. In order_line_items.csv, does line_total_usd ≈ unit_price_usd × quantity?
   ( on va devoir vérifier que c' est vrai pour cahque ligne )
   => oui c est le cas , sorti : True avec "print(((df["line_total_usd"] - df["unit_price_usd"] \* df["quantity"]).abs() < 0.0001).all())"

5. In reviews.jsonl, which columns start with \_? What do \_moderation_score and \_sentiment_raw look like?
   On a les champs suivants :

- moderation_score float64
- sentiment_raw float64
- toxicity_score float64
- language_detected str
- review_source str

Pour lees colonnes \_moderation_score et \_sentiment_raw sont des valeurs numeriques de type float comprises entre 0 et 1 ( je suppose), représentant respectivement un score de modération et un score de sentiment calculé automatiquement:
[5 rows x 20 columns]
0 0.3321
1 0.2997
2 0.4848
3 0.1966
4 0.8811
Name: \_moderation_score, dtype: float64
0 0.8989
1 0.7068
2 0.6897
3 0.9925
4 0.6270
Name: \_sentiment_raw, dtype: float64
(venv) ethan@ethan-Zenbook:~/Documents/

6. In the clickstream Parquet file, what does the event*type column contain? What *-columns exist?
   une seule valeur de event-type:
   ['pageview']
   Length: 1
   ( ce qui signifie que tous les événements correspondent à des vues de page)

Voici les columns :

- ga_client_id str
- gtm_container_id str
- dom_interactive_ms int64
- dom_complete_ms int64
- ttfb_ms int64
- connection_type str
- js_heap_size_mb float64
- consent_string str
