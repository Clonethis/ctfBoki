tvojeMama = " .   ..  ...  .  .. .... .. .. .  .      . . .   .. .    ..  . .  .      .   ... .. ..   .. .... ..   .  ..    . .. ..    .      .     . .. ...  ... .   .. .  .  . .. . . . .   ..  . . ...  .  ...  .  .. .... ...  .  .. .  . ...  .. ... .   ...  ..  .      . . .   ..    . ..   .. ... .   .. .  . ..   .. ...  ..    . .     . .  .  .  . ..  ..   .      ....  . .. .... ... . .  .      ...  .  ..  . . ..    . ..  .    .      ... .   .. .    .. .  . ...  ..  .      ....  . .. .... ... . .  .      ...     ..    . ...  .. ...  .. ..  . . ..  .    . ...   .      .    .. .. .... .. ...  ..  ... ...  .  ..    . ... .   ...  ..  . ...     . .  . ..  . .. .... ... . . ...  .   .      ..  ..  .. .  . ...  .  ...  .. ... .    .      ... .   ..    . ...  .. .. . ..  .      ... ... .. .  . .. ..   .. ..    .      ..   .. .. .... .. .. . ..  . .  .      ... .   .. .... .. .. . .. .... ...  .  ...  .  .. .... ... ...  . ...     . .  .   ... .. .... .. .... ..  .    .      .. ..   ... . . ..   .. .. . ..  . ...     . .     . .  .    .. . . .   .   ..  .. ..   ..  . . ..    . ...  .  .. ...  .... .. .  .  . ..  ..  . ..... ....  .  ..     ... . . . ..... ...  .   ..  ..  . .... . ...   ..  .   . ..... ... .   .. .    .. .  .  .. . . . ..... ....  . .. .... ... . . . ..... ...     ..    .  .. . .  .. . .  ..  .. ..  .   ..... ."
result = ""
for char in tvojeMama:
    # print("char: ", char)
    if char == " ":
        result += "0"
    else:
        result += "1"
print(result)
