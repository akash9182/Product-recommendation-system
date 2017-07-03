# Product-recommendation-system

It is a flask-based REST webservice designed to be deployed to Heroku and relies on Anaconda for the scientific computing dependencies, and Redis to store precomputed similarities. A production-ready, content-based recommendation engine that computes similar items based on text descriptions.

Work in progress for integrating other features.

# Results

    curl -X POST -H "X-API-TOKEN: FOOBAR1" -H "Content-Type: application/json; charset=utf-8" http://127.0.0.1:5000/predict -d "{"item":18,"num":10}"

```

For the below product our engine recommends 
3,"Active sport briefs - These superbreathable no-fly briefs are the minimalist's choice for high-octane endeavors. Made from a blend of fast-wicking, quick-drying 93% polyester (71% recycled) and 7% spandex that has both stretch-mesh (for support) and open mesh (for cooling airflow). Soft edging at the leg openings and a seamless waist won't roll or create friction against layers. With a smooth front panel for opacity. Recyclable through the Common Threads Recycling Program.

```

Predicts
```

[["2", 0.41816639921615745], ["299", 0.1140184812203873], ["495", 0.11053729446572887]]
ids ,probability of similarity

2,"Active sport boxer briefs - Skinning up Glory requires enough movement without your boxers deciding to poach their own route. The form-fitting Active Sport Boxer Briefs are made from breathable 93% polyester (71% recycled) fabric that's fast-wicking, dries quickly and has 7% spandex for stretch; the seamless waistband and soft leg edges won't roll or bind. The gusseted, flat-sewn 6"

299,"Active boy shorts - We've worn these versatile, feminine boy shorts as on-the-fly bathing suit bottoms, to Bikram yoga class, as sleepwear - their functionality is limitless. Low-rise Active Boy Shorts are tube-constructed to eliminate chafing side seams, and their soft, technical fabric breathes and wicks moisture to keep you comfortable and dry. We've shortened the flat waistband in front for a fit that won't roll or bind; stretchy shaped openings at legs are newly redesigned with less fabric to minimize bunching."

495,"Active briefs - These featherweight, quick-wicking briefs keep you comfortable and dry whether you travel by bus, kayak or stubborn yak. The nonbinding waistband is brushed for next-to-skin softness, and elastic in the leg openings provides a supple fit without constricting. With reversed-out stitching for chafe-free comfort, an easy-access, functional fly and a supportive front panel. Made from 100% polyester (54% recycled) with moisture-wicking performance and Gladiodor natural odor control for the garment. Recyclable through the Common Threads Recycling Program

```
Initial Source code used from [groveco](https://github.com/groveco/content-engine)
