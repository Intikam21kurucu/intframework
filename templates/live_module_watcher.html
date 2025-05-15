<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>intSpLoiT Live Module Watcher</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Global real-time module monitor powered by intframework." />
  <style>
    body {
      margin: 0;
      font-family: 'Courier New', monospace;
      background: linear-gradient(145deg, #0d0d0d, #1a1a1a);
      color: #00ffe1;
      overflow-x: hidden;
    }

    header {
      padding: 40px 20px;
      text-align: center;
      animation: fadeIn 2s ease-in;
    }

    header h1 {
      font-size: 2.5em;
      color: #ff00cc;
      text-shadow: 0 0 10px #ff00cc;
      animation: glow 2s infinite alternate;
      margin-bottom: 8px;
    }

    header p {
      font-style: italic;
      color: #aaa;
      margin-top: 0;
    }

    #search-container {
      max-width: 600px;
      margin: 20px auto;
      text-align: center;
      position: relative;
    }

    #search-box {
      width: 100%;
      padding: 12px 16px;
      border: none;
      border-radius: 25px;
      font-size: 1.1em;
      background: #121212;
      color: #00ffe1;
      box-shadow: 0 0 10px #00ffe1aa;
      outline: none;
      transition: box-shadow 0.3s ease;
      font-family: 'Courier New', monospace;
    }

    #search-box::placeholder {
      color: #00ffe1aa;
      font-style: italic;
    }

    #search-box:focus {
      box-shadow: 0 0 20px #ff00cc;
      color: #ff00cc;
    }

    #module-container {
      max-width: 100vw;
      margin: 30px auto 60px;
      padding: 10px 20px;
      display: flex;
      gap: 20px;
      overflow-x: auto;
      scroll-behavior: smooth;
      animation: slideRight 1.5s ease-in;
    }

    /* Hide scrollbar but still scrollable */
    #module-container::-webkit-scrollbar {
      height: 8px;
    }
    #module-container::-webkit-scrollbar-track {
      background: #121212;
    }
    #module-container::-webkit-scrollbar-thumb {
      background: #00ffe1cc;
      border-radius: 10px;
    }

    .module-box {
      flex: 0 0 300px; /* fixed width */
      background: #121212;
      border-left: 5px solid #00ffe1;
      padding: 20px;
      border-radius: 6px;
      box-shadow: 0 0 8px #00ffe144;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      cursor: pointer;
      color: #00ffe1;
    }

    .module-box:hover {
      transform: scale(1.05);
      box-shadow: 0 0 20px #ff00ccaa;
      border-left-color: #ff00cc;
      color: #ff00cc;
    }

    .module-box b {
      color: #ffdf00;
    }

    footer {
      text-align: center;
      padding: 30px;
      color: #888;
      font-size: 14px;
    }

    @keyframes glow {
      from {
        text-shadow: 0 0 5px #ff00cc, 0 0 10px #ff00cc;
      }
      to {
        text-shadow: 0 0 20px #ff00cc, 0 0 40px #ff00cc;
      }
    }

    @keyframes slideRight {
      from {
        transform: translateX(50px);
        opacity: 0;
      }
      to {
        transform: translateX(0);
        opacity: 1;
      }
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
      }
      to {
        opacity: 1;
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>intSpLoiT Live Module Watcher</h1>
    <p>Global real-time module monitor powered by intframework</p>
  </header>

  <div id="search-container">
    <input
      type="text"
      id="search-box"
      placeholder="Search modules, titles, descriptions..."
      autocomplete="off"
      spellcheck="false"
    />
  </div>

  <div id="module-container">
    <p>Loading modules...</p>
  </div>

  <footer>
    &copy; 2025 intSpLoiT Team — All rights reserved.
  </footer>

  <script>
    let modulesData = {};

    function renderModules(filter = '') {
      const container = document.getElementById('module-container');
      container.innerHTML = '';

      const filterLower = filter.toLowerCase();

      let filteredModules = Object.values(modulesData);

      if (filterLower) {
        filteredModules = filteredModules.filter(mod => {
          return (
            (mod.name && mod.name.toLowerCase().includes(filterLower)) ||
            (mod.title && mod.title.toLowerCase().includes(filterLower)) ||
            (mod.description && mod.description.toLowerCase().includes(filterLower))
          );
        });
      }

      if (filteredModules.length === 0) {
        container.innerHTML = '<p style="color:#ff0044; font-weight:bold;">No modules found matching your query.</p>';
        return;
      }

      filteredModules.forEach(mod => {
        const box = document.createElement('div');
        box.className = 'module-box';
        box.innerHTML = `
          <b>Module:</b> ${mod.name}<br>
          <b>Title:</b> ${mod.title || 'N/A'}<br>
          <b>Description:</b> ${mod.description || 'N/A'}<br>
          <b>Path:</b> ${mod.path}<br>
          <b>Language:</b> ${mod.language}<br>
          <b>Command:</b> ${mod.command}<br>
          <b>Author:</b> ${mod.author}<br>
          <b>Status:</b> ${mod.test_status}<br>
          <b>Size:</b> ${mod.size_kb} KB<br>
          <b>Last Modified:</b> ${mod.last_modified}
        `;
        container.appendChild(box);
      });
    }

    fetch('https://raw.githubusercontent.com/intSpLoiT/intframework/refs/heads/%C4%B0ntframeworkV4/db/modules.json')
      .then(res => res.json())
      .then(data => {
        modulesData = data;
        renderModules();
      })
      .catch(err => {
        document.getElementById('module-container').innerHTML = `<p style="color: red;">Failed to load modules.</p>`;
        console.error(err);
      });

    document.getElementById('search-box').addEventListener('input', e => {
      renderModules(e.target.value);
    });
  </script>
</body>
</html>