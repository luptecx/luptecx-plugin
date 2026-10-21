# luptecx-bot-whatsapp (opcional)

Reglas que solo sirven a los proyectos que conversan por WhatsApp con la Cloud API de Meta.
Van aparte del plugin general `luptecx` para que ninguna skill general cargue lo de un tipo
de proyecto.

Se activa por proyecto, en su `.claude/settings.json`:

```json
"enabledPlugins": {
  "luptecx@luptecx": true,
  "luptecx-bot-whatsapp@luptecx": true
}
```

Cuando aparezca otro tipo de proyecto que se repita (por ejemplo, agentes con IA), sus
reglas van en un plugin aparte como este, después de construir el primero y no antes.
