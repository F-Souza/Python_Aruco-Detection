# Python_Aruco-Detection

- Importando as bibliotecas necessárias.

      import cv2

      import cv2.aruco as aruco

- Iniciando a Câmera/WebCam.

      cap = cv2.VideoCapture(0) 
        
- Pegando a Imagem/Frames.

      while True:
        
        ret, frame = cap.read()
        
      # Usando o aruco para detectar marcas de 6x6.

        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        
      # Pegando os parâmetros.
        
        parameters =  aruco.DetectorParameters_create()

      # E apartir disso, pegamos os cantos (corners) da Aruco Mark detectada e  os _ids e rejectedImgPoints_ que 
      podem ser ignorados por enquanto. Por agora, importante mesmo só a corners, porque ela é quem vai nos 
      retornar a posição dos cantos da Aruco Mark na imagem.

        corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        
      # E por fim, "desenhamos" na tela (frame) os cantos que encontramos.

        frame_detected = aruco.drawDetectedMarkers(frame, corners)
        
      # E mostramos.
        
        cv2.imshow('frame',frame_detected)

      # Verificação de key para parar de pegar as imagens (frame) da WebCam.

        if cv2.waitKey(1) & 0xFF == ord('q'):
        
            break

- No Fim, damos release na imagem e fechamos a janela da WebCam.

      cap.release()

      cv2.destroyAllWindows()


