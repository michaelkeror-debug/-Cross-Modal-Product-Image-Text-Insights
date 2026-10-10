from mismatch import bow, cosine, tokens


def search(query, catalog, k=3):
    qv = bow(tokens(query))
    scored = []
    for row in catalog:
        iv = bow(row.get('image_tags') or [])
        scored.append((cosine(qv, iv), row['sku']))
    scored.sort(reverse=True)
    return scored[:k]


def top_skus(query, catalog, k=3):
    """query -> top-k SKUs (no scores), best match first."""
    return [sku for _, sku in search(query, catalog, k)]


def recall_at_k(query, catalog, relevant, k=3):
    """Fraction of the relevant SKUs that appear in the top-k results."""
    hits = set(top_skus(query, catalog, k)) & set(relevant)
    return len(hits) / len(relevant)


if __name__ == '__main__':
    demo_catalog = [
        {'sku': 'KND-01', 'image_tags': ['kiondo', 'bag', 'sisal', 'navy']},
        {'sku': 'NK-99', 'image_tags': ['kiondo', 'bag']},
    ]
    results = search('navy sisal kiondo', demo_catalog, k=2)
    assert results[0][1] == 'KND-01'
    print('search(\'navy sisal kiondo\') =', results)

    # Toy recall check: the only relevant SKU for this query is KND-01.
    # Cosine scores: KND-01 ~= 0.87 (3 of 3 query terms match), NK-99 ~= 0.41
    # (1 of 3), so KND-01 ranks first and recall@1 = 1/1 = 1.0.
    # With k=2 both SKUs are returned, so recall@2 is also 1.0 (precision drops).
    print('top_skus =', top_skus('navy sisal kiondo', demo_catalog, k=1))
    assert recall_at_k('navy sisal kiondo', demo_catalog, {'KND-01'}, k=1) == 1.0
    print('recall@1 =', recall_at_k('navy sisal kiondo', demo_catalog, {'KND-01'}, k=1))
