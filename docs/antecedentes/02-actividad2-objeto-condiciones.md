> **Antecedente:** Actividad 2, Identificación del objeto de prueba y condiciones (versión final entregada, con coevaluación del equipo de RESTful Booker).

# Actividad 2 - Objeto de prueba y condiciones

## 2. Identificación del objeto de prueba

| ID | Elemento | ¿Qué hace? / Actor | ¿Alcance? | Justificación |
|---|---|---|---|---|
| F01 | Inicio de sesión | Permite el ingreso al sistema con usuario y contraseña. / Todos los usuarios | Sí | Controla el acceso general al sistema. |
| F02 | Gestión de usuarios y roles | Crea usuarios, les asigna un rol y define qué puede ver o modificar cada uno. / Administrador | Sí | Garantiza que cada usuario acceda solo a la información que le corresponde. |
| F03 | Registro del seguimiento a docentes | Permite evaluar los criterios de cada curso en cada revisión del semestre y registrar observaciones. / Revisor | Sí | Es la función principal del sistema y la fuente de los datos de las métricas. |
| F04 | Semáforo de cumplimiento | Clasifica cada curso en verde, amarillo o rojo según el porcentaje de criterios cumplidos. / Líderes académicos | Sí | Resume el estado del seguimiento y apoya la toma de decisiones. |
| F05 | Panel de métricas | Muestra estadísticas del seguimiento por departamento y por revisión. / Líderes académicos, administrador | Sí | Permite validar que la información presentada sea confiable. |
| F06 | Exportación de informes | Genera un informe en Excel con los resultados del seguimiento. / Revisor, líderes académicos | Sí | Es la salida formal de la información y debe coincidir con lo registrado en el sistema. |

## 3. Condiciones de prueba

| ID | Precondiciones / Datos de entrada | Resultado esperado |
|---|---|---|
| F02 | Existe un usuario con un rol de solo consulta. Ese usuario intenta modificar un registro de seguimiento. | El sistema impide la modificación y muestra un mensaje de acceso denegado. El usuario solo puede ver la información. |
| F03 | El revisor ha iniciado sesión y existe un curso asignado en una revisión abierta. El revisor marca los criterios y escribe una observación. | La información queda guardada, se asocia al curso y a la revisión correctos, y se ve igual al volver a consultarla. |
| F04 | Existen tres cursos evaluados en la misma revisión: uno con el 80 % de los criterios cumplidos, otro con el 50 % y otro con el 40 %. | El semáforo muestra verde, amarillo y rojo, respectivamente. |

## 4. Priorización

| Prioridad | Elemento | Justificación |
|---|---|---|
| 1 (Alta) | F02 Gestión de usuarios y roles | Tiene el mayor impacto ante fallas: un error en los permisos permitiría ver o modificar información de otros usuarios o departamentos. |
| 2 (Media) | F03 Registro del seguimiento | Es la funcionalidad de mayor frecuencia de uso, y los errores en el registro afectan todos los resultados posteriores. |
| 3 (Media) | F04 Semáforo de cumplimiento | Es crítico para el usuario, porque los líderes toman decisiones con base en este resultado. Un cálculo incorrecto genera conclusiones equivocadas. |

## 6. Ajustes y reflexión

**Ajustes tras la coevaluación:** el equipo revisor no reportó oportunidades de mejora. En la autorrevisión se completó F06 (Exportación de informes) para cumplir el mínimo de 6 funcionalidades.

**Reflexión:** sin saber qué es más importante probar, se pierde esfuerzo en casos innecesarios y se descuidan las funciones críticas del sistema.
