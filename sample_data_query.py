sample_data = """ 
INSERT INTO production_data (
    station_name,
    model_type,
    batch_number,
    tray_number,
    product_line,
    supplier_name,
    ok_quantity,
    ng_quantity,
    operator_name,
    remarks,
    production_date
)
SELECT
    station_list[(g % array_length(station_list, 1)) + 1] AS station_name,
    CASE WHEN random() > 0.5 THEN 'TX' ELSE 'RX' END AS model_type,
    (100 + (g / 18))::INT AS batch_number,
    (g % 10) + 1 AS tray_number,
    product_line_list[(g % array_length(product_line_list, 1)) + 1],
    supplier_list[(g % array_length(supplier_list, 1)) + 1],
    (900 + (random() * 200)::INT) AS ok_quantity,
    (random() * 10)::INT AS ng_quantity,
    operator_list[(g % array_length(operator_list, 1)) + 1],
    CASE
        WHEN random() < 0.1 THEN 'Rework'
        WHEN random() < 0.2 THEN 'Minor NG'
        ELSE ''
    END AS remarks,
    TIMESTAMP '2026-01-12 08:00:00' + (g * INTERVAL '2 hour') AS production_date
FROM generate_series(0, 119) AS g
CROSS JOIN (
    SELECT ARRAY[
        'Incoming Check',
        'Module Dispensing',
        'UV Curing dispense',
        'IC Bonding',
        'Pd/VC Bonding',
        'Wire Bonding',
        'Wire Checking',
        'Lens Bonding',
        'Lens CCD Position Check',
        'U Lens',
        'Bake/Oven',
        'Upload Program',
        'Divide Board',
        'Labeling',
        'BERT Test',
        'Dispensing Reverse',
        'Check Connector',
        'Packing'
    ] AS station_list,
    ARRAY['Indo #1', 'Indo #2', 'Line A', 'Line B'] AS product_line_list,
    ARRAY['Ryuhan', 'YungSheng', 'KeiKou', 'JVC', 'Other'] AS supplier_list,
    ARRAY[
        'TRI NOVRIYANSYAH',
        'JASMAN',
        'SITI DEWI RINAZAH',
        'YAP LIDIANA',
        'ROSWANTI HERDIANTI',
        'RANA SAPUTRA',
        'AINI LATIFAH',
        'SYIFA ALFIA',
        'NADIA PERMATASARI'
    ] AS operator_list
) master_data;
"""