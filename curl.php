<?php
// $url = 'http://127.0.0.1:5000/';
// $data = array('key1' => 'value1', 'key2' => 'value2');

// // use key 'http' even if you send the request to https://...
// $options = array(
//     'http' => array(
//         'header'  => "Content-type: application/json\r\n",
//         'method'  => 'POST',
//         'content' => http_build_query($data)
//     )
// );
// $context  = stream_context_create($options);
// $result = file_get_contents($url,FALSE, $context);
// if ($result === FALSE) { /* Handle error */ }

// var_dump($result);

// set post fields
// $post = [
//     'username' => 'user1',
//     'password' => 'passuser1',
//     'gender'   => 1,
// ];

// $ch = curl_init('http://127.0.0.1:5000');
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// curl_setopt($ch, CURLOPT_POSTFIELDS, $post);

// // execute!
// $response = curl_exec($ch);

// // close the connection, release resources used
// curl_close($ch);

// // do anything you want with your response
// var_dump($response);

$url = 'http://127.0.0.1:5000';
$data = array('filepath' => 'C:\Users\pb7n0079\Desktop\pip\Writing a Thesis.docx', 'filename' => 'value2');

// use key 'http' even if you send the request to https://...
$options = array(
    'http' => array(
        'header'  => "Content-type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

echo($result);

?>