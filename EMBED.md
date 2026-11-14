# Put a remaining-send check on a workshop resource page

For independent course and workshop facilitators who already have an email sending allowance. Let a reader check whether the next announcement, planned repeats and other sends fit the balance left before the same reset. This worksheet does not send email or connect to an account.

## Try it before you copy it

[Open the served standalone worksheet](https://send-budget-1109.crisp-llama-2628.chatgpt.site/embed/remaining-sends.html). Its initial counts are an example. Try remaining **450**, next campaign **200**, reserved resends **100**, and other sends **200**: needed **500**, balance **−50**, shortfall **50**. Then clear a field: blank means unknown, not zero. Enter an explicit **0** when you assume none.

You enter the four counts inside the worksheet. The embed has no URL prefilling, parent-page input API or postMessage integration. It does not verify provider counters, reset times, daily limits, sending speed, delivery or fees, and does not recommend a plan.

## Copy onto an HTTP(S) page

Your publishing tool must permit iframes. Put the snippet below in its HTML/embed component and preview it on the actual page. The served widget permits HTTP(S) parents; a downloaded wrapper opened directly as `file://` is not a supported embedding test. It needs an internet connection and is not an offline calculator.

```html
<iframe
  src="https://send-budget-1109.crisp-llama-2628.chatgpt.site/embed/remaining-sends.html"
  title="Remaining-send balance calculator by Send Budget"
  style="width:100%;height:1000px;border:0"
  loading="lazy"
  referrerpolicy="no-referrer"
  sandbox="allow-scripts"></iframe>
<p><a href="https://send-budget-1109.crisp-llama-2628.chatgpt.site/capacity.html?utm_source=embed&amp;utm_medium=widget#remaining-send-balance" rel="noreferrer">Open the full remaining-send calculator on Send Budget</a></p>
```

Keep the iframe title, `referrerpolicy` and minimal sandbox. The widget only needs `allow-scripts`; do not add `allow-same-origin`, popup or form permission to make this example work. Keep scrolling enabled. Adjust the height in your actual editor if necessary and check all controls and result text at both narrow and wide widths. An ordinary full-tool link stays outside the frame for readers whose editor or browser blocks embedding. GitHub renders this guide as documentation; it does not run this iframe inside the README.

[Example host-page source](examples/remaining-send-balance-embed.html) puts the same iframe in a small page with the code and a fallback link. Download or copy it into an HTTP(S) website you control. Raw GitHub source is not a hosted interactive demo. No new account, paid subscription, email list or recipient details are needed to use the calculation.

## What loads and what is measured

The iframe requests the public worksheet HTML, CSS and calculation script from Send Budget. The four numbers remain in the iframe page's memory. Its application code has no input upload, saved entries, analytics, referral advertising or URL prefilling. Serving the files still involves ordinary network requests and hosting logs; this is not a claim of zero communication. Your surrounding website has its own privacy behavior.

The optional full-tool link outside the frame uses the existing `utm_source=embed&utm_medium=widget` marker. The current full-tool application can record fixed anonymous aggregate categories; this marker is a broad category, not a visitor identifier or proof of a particular publisher's adoption. No marker or analytics is added to the iframe itself.

I maintain Send Budget and this resource, and used AI assistance to prepare them. Separate full-tool pages include optional labelled systeme.io referral advertising; eligible referrals may compensate me. The embedded worksheet contains no referral link or ad, and no referral click or purchase is required. This example embeds the existing served tool; it does not distribute or license the hosted application's source code.

The Japanese v1.0.0 and English v1.1.0 workshop planning downloads remain separate and unchanged. This capacity check does not import, synchronize or alter those documents.
