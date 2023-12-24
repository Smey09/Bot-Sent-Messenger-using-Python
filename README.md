<h1>Bot-Sent-Messenger-using-Python</h1>

<h2>How to install and run this code:</h2>

<p><strong>Prerequisite:</strong> Make sure you have Python installed on your device.</p>

<h3>Step 1</h3>

<p>Download this code.</p>

<h3>Step 2</h3>

<p>Open your code editor (VS Code, PyCharm, etc.).</p>

<h3>Step 3</h3>

<p>Set up the code for your environment:</p>

<ol>
  <li>Open a terminal or command prompt.</li>
  <li>Install required libraries:
    <pre><code>pip install webdriver
pip install selenium
    </code></pre>
    <em>(If you encounter "zsh: command not found: pip", try to run:)</em>
    <pre><code>pip3 install webdriver
pip3 install selenium
    </code></pre>
  </li>
</ol>

<h3>Step 4</h3>

<p>Update your information:</p>

<ol>
  <li>In the <code>FacebookAccountInfo.py</code> file:
    <ul>
      <li>Enter your Gmail and Facebook password:
        <pre><code># input your email
username = 'YourGmail@gmail.com'
# input your password
password = 'YourFacebookPassword'
        </code></pre>
      </li>
    </ul>
  </li>
  <li>In the <code>MessengerBot_Optimized.py</code> file:
    <ul>
      <li>On line 74, modify the message details:
        <pre><code>bot1.SendMessageTo('FriendName', 'MessageText', NumberOfMessages)
        </code></pre>
        <ul>
          <li><code>FriendName</code>: Replace with your friend's name on Facebook.</li>
          <li><code>MessageText</code>: Replace with the text you want to send.</li>
          <li><code>NumberOfMessages</code>: Specify the number of messages to send.</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>

<h3>Step 5</h3>

<p>Run the code:</p>

<ol>
  <li>Execute the code in your editor.(Run Code)</li>
  <li>If you see a notification, click "OK".</li>
  <li>How to fix this notification on macOS:
    <ol>
      <li>Open Mac Setting.</li>
      <li>Go to 'Privacy & Security'.</li>
      <li>Scroll down and click "Allow Anyway".</li>
      <img width="496" alt="Pro" src="https://github.com/Smey09/My-Image/assets/149933218/62fa744a-4c33-4717-bb74-a1c8d9a3cf64">
    </ol>
  </li>
</ol>
