const CACHE_NAME = 'expense-tracker-v1';
const STATIC_ASSETS = [
  '/static/manifest.json',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);

  // Never cache HTML pages or POST requests - always fetch from network
  if (e.request.method !== 'GET' || !url.pathname.startsWith('/static/')) {
    e.respondWith(fetch(e.request));
    return;
  }

  // Only cache static files
  e.respondWith(
    caches.match(e.request).then((cached) => cached || fetch(e.request))
  );
});