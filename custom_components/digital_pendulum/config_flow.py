import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector

from .const import (
    DOMAIN,
    CONF_START_HOUR,
    CONF_END_HOUR,
    CONF_PLAYER_DEVICE,
    CONF_ENABLED,
    CONF_USE_CHIME,
    CONF_CUSTOM_CHIME_PATH,
    CONF_PRESET_CHIME,  
    DEFAULT_START_HOUR,
    DEFAULT_END_HOUR,
    DEFAULT_ENABLED,
    DEFAULT_USE_CHIME,
    DEFAULT_CUSTOM_CHIME_PATH,
    DEFAULT_PRESET_CHIME, 
    PRESET_CHIMES,  
)


class DigitalPendulumConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle initial configuration."""
        if user_input is not None:
            return self.async_create_entry(
                title="Digital Pendulum",
                data=user_input,
            )

        # Crea lista opzioni per dropdown
        chime_options = [
            selector.SelectOptionDict(value=key, label=info["name"])
            for key, info in PRESET_CHIMES.items()
        ]

        schema = vol.Schema(
            {
                vol.Required(
                    CONF_PLAYER_DEVICE
                ): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="media_player",
                        integration="alexa_media"
                    )
                ),
                vol.Required(
                    CONF_START_HOUR,
                    default=DEFAULT_START_HOUR,
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=0,
                        max=23,
                        mode=selector.NumberSelectorMode.BOX,
                    )
                ),
                vol.Required(
                    CONF_END_HOUR,
                    default=DEFAULT_END_HOUR,
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=0,
                        max=23,
                        mode=selector.NumberSelectorMode.BOX,
                    )
                ),
                vol.Required(
                    CONF_ENABLED,
                    default=DEFAULT_ENABLED,
                ): bool,
                vol.Required(
                    CONF_USE_CHIME,
                    default=DEFAULT_USE_CHIME,
                ): bool,
                #-- Dropdown suoni predefiniti
                vol.Required(
                    CONF_PRESET_CHIME,
                    default=DEFAULT_PRESET_CHIME,
                ): selector.SelectSelector(
                    selector.SelectSelectorConfig(
                        options=chime_options,
                        mode=selector.SelectSelectorMode.DROPDOWN,
                    )
                ),
                # ← Campo custom path (visibile solo se selezione "custom")
                vol.Optional(
                    CONF_CUSTOM_CHIME_PATH,
                    default=DEFAULT_CUSTOM_CHIME_PATH,
                ): selector.TextSelector(
                    selector.TextSelectorConfig(
                        type=selector.TextSelectorType.TEXT,
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return DigitalPendulumOptionsFlow(config_entry)


class DigitalPendulumOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Digital Pendulum."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current_options = self.entry.options or self.entry.data

        #-- Crea lista opzioni per dropdown
        chime_options = [
            selector.SelectOptionDict(value=key, label=info["name"])
            for key, info in PRESET_CHIMES.items()
        ]

        schema = vol.Schema(
            {
                vol.Required(
                    CONF_PLAYER_DEVICE,
                    default=current_options.get(CONF_PLAYER_DEVICE)
                ): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="media_player",
                        integration="alexa_media"
                    )
                ),
                vol.Required(
                    CONF_START_HOUR,
                    default=current_options.get(CONF_START_HOUR, DEFAULT_START_HOUR),
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=0,
                        max=23,
                        mode=selector.NumberSelectorMode.BOX,
                    )
                ),
                vol.Required(
                    CONF_END_HOUR,
                    default=current_options.get(CONF_END_HOUR, DEFAULT_END_HOUR),
                ): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=0,
                        max=23,
                        mode=selector.NumberSelectorMode.BOX,
                    )
                ),
                vol.Required(
                    CONF_USE_CHIME,
                    default=current_options.get(CONF_USE_CHIME, DEFAULT_USE_CHIME),
                ): bool,
                #--- Dropdown suoni
                vol.Required(
                    CONF_PRESET_CHIME,
                    default=current_options.get(CONF_PRESET_CHIME, DEFAULT_PRESET_CHIME),
                ): selector.SelectSelector(
                    selector.SelectSelectorConfig(
                        options=chime_options,
                        mode=selector.SelectSelectorMode.DROPDOWN,
                    )
                ),
                vol.Optional(
                    CONF_CUSTOM_CHIME_PATH,
                    default=current_options.get(CONF_CUSTOM_CHIME_PATH, DEFAULT_CUSTOM_CHIME_PATH),
                ): selector.TextSelector(
                    selector.TextSelectorConfig(
                        type=selector.TextSelectorType.TEXT,
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=schema,
        )