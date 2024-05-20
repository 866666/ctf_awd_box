import zwsp_steg

encoded = zwsp_steg.encode("hidden message")
encoded = "‌‌‌‌‍‬‍‬‌‌‌‌‍‬﻿‌Before ‌‌‌‌‍‬‌‍‌‌‌‌‍‬‍﻿‌‌‌‌‍﻿‬﻿‌‌‌‌‍‬‍‬1‌‌‌‌‍‬‍‍,‌‌‌‌‍‬﻿‬ the‌‌‌‌‍‬﻿﻿ ‌‌‌‌‍‬‍‌‌‌‌‌‍‬‬‍‌‌‌‌‍﻿‍‬number‌‌‌‌‍‬‌‬‌‌‌‌‍‬‍‍‌‌‌‌‍‬﻿‬‌‌‌‌‍‬‍‌‌‌‌‌‍﻿‌‌ ‌‌‌‌‍‬‬‍is ‌‌‌‌‍﻿‌﻿‌‌‌‌‍‬﻿‬‌‌‌‌‍﻿‍‬‌‌‌‌‍‬‍‍‌‌‌‌‍﻿‌‌‌‌‌‌‍﻿﻿‍0."
decoded = zwsp_steg.decode(encoded)

print(decoded)  # hidden message
