csr = {
    'dna_dna': (28, 0x000, 64, False),
    'fast_a_x_tap': (0, 0x000, 2, True),
    'fast_a_brk': (0, 0x001, 1, True),
    'fast_a_y_tap': (0, 0x002, 2, True),
    'fast_a_iir_a_z0': (0, 0x003, 27, True),
    'fast_a_iir_a_shift': (0, 0x007, 5, False),
    'fast_a_iir_a_width': (0, 0x008, 5, False),
    'fast_a_iir_a_interval': (0, 0x009, 8, False),
    'fast_a_iir_a_a1': (0, 0x00a, 18, True),
    'fast_a_iir_a_b0': (0, 0x00d, 18, True),
    'fast_a_iir_a_b1': (0, 0x010, 18, True),
    'fast_a_demod_delay': (0, 0x013, 14, True),
    'fast_a_iir_b_z0': (0, 0x015, 38, True),
    'fast_a_iir_b_shift': (0, 0x01a, 5, False),
    'fast_a_iir_b_width': (0, 0x01b, 5, False),
    'fast_a_iir_b_interval': (0, 0x01c, 8, False),
    'fast_a_iir_b_a1': (0, 0x01d, 25, True),
    'fast_a_iir_b_a2': (0, 0x021, 25, True),
    'fast_a_iir_b_b0': (0, 0x025, 25, True),
    'fast_a_iir_b_b1': (0, 0x029, 25, True),
    'fast_a_iir_b_b2': (0, 0x02d, 25, True),
    'fast_a_x_limit_min': (0, 0x031, 25, True),
    'fast_a_x_limit_max': (0, 0x035, 25, True),
    'fast_a_iir_c_z0': (0, 0x039, 27, True),
    'fast_a_iir_c_shift': (0, 0x03d, 5, False),
    'fast_a_iir_c_width': (0, 0x03e, 5, False),
    'fast_a_iir_c_interval': (0, 0x03f, 8, False),
    'fast_a_iir_c_a1': (0, 0x040, 18, True),
    'fast_a_iir_c_b0': (0, 0x043, 18, True),
    'fast_a_iir_c_b1': (0, 0x046, 18, True),
    'fast_a_iir_d_z0': (0, 0x049, 27, True),
    'fast_a_iir_d_shift': (0, 0x04d, 5, False),
    'fast_a_iir_d_width': (0, 0x04e, 5, False),
    'fast_a_iir_d_interval': (0, 0x04f, 8, False),
    'fast_a_iir_d_a1': (0, 0x050, 18, True),
    'fast_a_iir_d_a2': (0, 0x053, 18, True),
    'fast_a_iir_d_b0': (0, 0x056, 18, True),
    'fast_a_iir_d_b1': (0, 0x059, 18, True),
    'fast_a_iir_d_b2': (0, 0x05c, 18, True),
    'fast_a_iir_e_z0': (0, 0x05f, 38, True),
    'fast_a_iir_e_shift': (0, 0x064, 5, False),
    'fast_a_iir_e_width': (0, 0x065, 5, False),
    'fast_a_iir_e_interval': (0, 0x066, 8, False),
    'fast_a_iir_e_a1': (0, 0x067, 25, True),
    'fast_a_iir_e_a2': (0, 0x06b, 25, True),
    'fast_a_iir_e_b0': (0, 0x06f, 25, True),
    'fast_a_iir_e_b1': (0, 0x073, 25, True),
    'fast_a_iir_e_b2': (0, 0x077, 25, True),
    'fast_a_relock_shift': (0, 0x07b, 5, False),
    'fast_a_relock_step': (0, 0x07c, 24, True),
    'fast_a_relock_run': (0, 0x07f, 1, True),
    'fast_a_relock_min': (0, 0x080, 15, True),
    'fast_a_relock_max': (0, 0x082, 15, True),
    'fast_a_sweep_shift': (0, 0x084, 5, False),
    'fast_a_sweep_step': (0, 0x085, 24, True),
    'fast_a_sweep_min': (0, 0x088, 14, True),
    'fast_a_sweep_max': (0, 0x08a, 14, True),
    'fast_a_sweep_run': (0, 0x08c, 1, True),
    'fast_a_mod_amp': (0, 0x08d, 14, True),
    'fast_a_mod_freq': (0, 0x08f, 32, True),
    'fast_a_y_limit_min': (0, 0x093, 14, True),
    'fast_a_y_limit_max': (0, 0x095, 14, True),
    'fast_a_x_clr': (0, 0x097, 1, True),
    'fast_a_x_max': (0, 0x098, 25, False),
    'fast_a_x_min': (0, 0x09c, 25, False),
    'fast_a_y_clr': (0, 0x0a0, 1, True),
    'fast_a_y_max': (0, 0x0a1, 25, False),
    'fast_a_y_min': (0, 0x0a5, 25, False),
    'fast_a_x_hold_en': (0, 0x0a9, 27, True),
    'fast_a_x_clear_en': (0, 0x0ad, 27, True),
    'fast_a_y_hold_en': (0, 0x0b1, 27, True),
    'fast_a_y_clear_en': (0, 0x0b5, 27, True),
    'fast_a_relock_en': (0, 0x0b9, 27, True),
    'fast_a_dx_sel': (0, 0x0bd, 4, True),
    'fast_a_dy_sel': (0, 0x0be, 4, True),
    'fast_a_rx_sel': (0, 0x0bf, 4, True),
    'fast_b_x_tap': (1, 0x000, 2, True),
    'fast_b_brk': (1, 0x001, 1, True),
    'fast_b_y_tap': (1, 0x002, 2, True),
    'fast_b_iir_a_z0': (1, 0x003, 27, True),
    'fast_b_iir_a_shift': (1, 0x007, 5, False),
    'fast_b_iir_a_width': (1, 0x008, 5, False),
    'fast_b_iir_a_interval': (1, 0x009, 8, False),
    'fast_b_iir_a_a1': (1, 0x00a, 18, True),
    'fast_b_iir_a_b0': (1, 0x00d, 18, True),
    'fast_b_iir_a_b1': (1, 0x010, 18, True),
    'fast_b_demod_delay': (1, 0x013, 14, True),
    'fast_b_iir_b_z0': (1, 0x015, 38, True),
    'fast_b_iir_b_shift': (1, 0x01a, 5, False),
    'fast_b_iir_b_width': (1, 0x01b, 5, False),
    'fast_b_iir_b_interval': (1, 0x01c, 8, False),
    'fast_b_iir_b_a1': (1, 0x01d, 25, True),
    'fast_b_iir_b_a2': (1, 0x021, 25, True),
    'fast_b_iir_b_b0': (1, 0x025, 25, True),
    'fast_b_iir_b_b1': (1, 0x029, 25, True),
    'fast_b_iir_b_b2': (1, 0x02d, 25, True),
    'fast_b_x_limit_min': (1, 0x031, 25, True),
    'fast_b_x_limit_max': (1, 0x035, 25, True),
    'fast_b_iir_c_z0': (1, 0x039, 27, True),
    'fast_b_iir_c_shift': (1, 0x03d, 5, False),
    'fast_b_iir_c_width': (1, 0x03e, 5, False),
    'fast_b_iir_c_interval': (1, 0x03f, 8, False),
    'fast_b_iir_c_a1': (1, 0x040, 18, True),
    'fast_b_iir_c_b0': (1, 0x043, 18, True),
    'fast_b_iir_c_b1': (1, 0x046, 18, True),
    'fast_b_iir_d_z0': (1, 0x049, 27, True),
    'fast_b_iir_d_shift': (1, 0x04d, 5, False),
    'fast_b_iir_d_width': (1, 0x04e, 5, False),
    'fast_b_iir_d_interval': (1, 0x04f, 8, False),
    'fast_b_iir_d_a1': (1, 0x050, 18, True),
    'fast_b_iir_d_a2': (1, 0x053, 18, True),
    'fast_b_iir_d_b0': (1, 0x056, 18, True),
    'fast_b_iir_d_b1': (1, 0x059, 18, True),
    'fast_b_iir_d_b2': (1, 0x05c, 18, True),
    'fast_b_iir_e_z0': (1, 0x05f, 38, True),
    'fast_b_iir_e_shift': (1, 0x064, 5, False),
    'fast_b_iir_e_width': (1, 0x065, 5, False),
    'fast_b_iir_e_interval': (1, 0x066, 8, False),
    'fast_b_iir_e_a1': (1, 0x067, 25, True),
    'fast_b_iir_e_a2': (1, 0x06b, 25, True),
    'fast_b_iir_e_b0': (1, 0x06f, 25, True),
    'fast_b_iir_e_b1': (1, 0x073, 25, True),
    'fast_b_iir_e_b2': (1, 0x077, 25, True),
    'fast_b_relock_shift': (1, 0x07b, 5, False),
    'fast_b_relock_step': (1, 0x07c, 24, True),
    'fast_b_relock_run': (1, 0x07f, 1, True),
    'fast_b_relock_min': (1, 0x080, 15, True),
    'fast_b_relock_max': (1, 0x082, 15, True),
    'fast_b_sweep_shift': (1, 0x084, 5, False),
    'fast_b_sweep_step': (1, 0x085, 24, True),
    'fast_b_sweep_min': (1, 0x088, 14, True),
    'fast_b_sweep_max': (1, 0x08a, 14, True),
    'fast_b_sweep_run': (1, 0x08c, 1, True),
    'fast_b_mod_amp': (1, 0x08d, 14, True),
    'fast_b_mod_freq': (1, 0x08f, 32, True),
    'fast_b_y_limit_min': (1, 0x093, 14, True),
    'fast_b_y_limit_max': (1, 0x095, 14, True),
    'fast_b_x_clr': (1, 0x097, 1, True),
    'fast_b_x_max': (1, 0x098, 25, False),
    'fast_b_x_min': (1, 0x09c, 25, False),
    'fast_b_y_clr': (1, 0x0a0, 1, True),
    'fast_b_y_max': (1, 0x0a1, 25, False),
    'fast_b_y_min': (1, 0x0a5, 25, False),
    'fast_b_x_hold_en': (1, 0x0a9, 27, True),
    'fast_b_x_clear_en': (1, 0x0ad, 27, True),
    'fast_b_y_hold_en': (1, 0x0b1, 27, True),
    'fast_b_y_clear_en': (1, 0x0b5, 27, True),
    'fast_b_relock_en': (1, 0x0b9, 27, True),
    'fast_b_dx_sel': (1, 0x0bd, 4, True),
    'fast_b_dy_sel': (1, 0x0be, 4, True),
    'fast_b_rx_sel': (1, 0x0bf, 4, True),
    'gpio_n_ins': (30, 0x000, 8, False),
    'gpio_n_outs': (30, 0x001, 8, True),
    'gpio_n_oes': (30, 0x002, 8, True),
    'gpio_n_state': (30, 0x003, 27, False),
    'gpio_n_state_clr': (30, 0x007, 1, True),
    'gpio_n_do0_en': (30, 0x008, 27, True),
    'gpio_n_do1_en': (30, 0x00c, 27, True),
    'gpio_n_do2_en': (30, 0x010, 27, True),
    'gpio_n_do3_en': (30, 0x014, 27, True),
    'gpio_n_do4_en': (30, 0x018, 27, True),
    'gpio_n_do5_en': (30, 0x01c, 27, True),
    'gpio_n_do6_en': (30, 0x020, 27, True),
    'gpio_n_do7_en': (30, 0x024, 27, True),
    'gpio_p_ins': (31, 0x000, 8, False),
    'gpio_p_outs': (31, 0x001, 8, True),
    'gpio_p_oes': (31, 0x002, 8, True),
    'noise_bits': (7, 0x000, 5, True),
    'noise_y_clr': (7, 0x001, 1, True),
    'noise_y_max': (7, 0x002, 25, False),
    'noise_y_min': (7, 0x006, 25, False),
    'scopegen_dac_a_clr': (6, 0x000, 1, True),
    'scopegen_dac_a_max': (6, 0x001, 25, False),
    'scopegen_dac_a_min': (6, 0x005, 25, False),
    'scopegen_dac_b_clr': (6, 0x009, 1, True),
    'scopegen_dac_b_max': (6, 0x00a, 25, False),
    'scopegen_dac_b_min': (6, 0x00e, 25, False),
    'scopegen_adc_a_sel': (6, 0x012, 4, True),
    'scopegen_adc_b_sel': (6, 0x013, 4, True),
    'slow_a_brk': (2, 0x000, 1, True),
    'slow_a_x_limit_min': (2, 0x001, 25, True),
    'slow_a_x_limit_max': (2, 0x005, 25, True),
    'slow_a_iir_z0': (2, 0x009, 38, True),
    'slow_a_iir_shift': (2, 0x00e, 5, False),
    'slow_a_iir_width': (2, 0x00f, 5, False),
    'slow_a_iir_interval': (2, 0x010, 8, False),
    'slow_a_iir_a1': (2, 0x011, 25, True),
    'slow_a_iir_a2': (2, 0x015, 25, True),
    'slow_a_iir_b0': (2, 0x019, 25, True),
    'slow_a_iir_b1': (2, 0x01d, 25, True),
    'slow_a_iir_b2': (2, 0x021, 25, True),
    'slow_a_y_limit_min': (2, 0x025, 16, True),
    'slow_a_y_limit_max': (2, 0x027, 16, True),
    'slow_a_x_clr': (2, 0x029, 1, True),
    'slow_a_x_max': (2, 0x02a, 25, False),
    'slow_a_x_min': (2, 0x02e, 25, False),
    'slow_a_y_clr': (2, 0x032, 1, True),
    'slow_a_y_max': (2, 0x033, 25, False),
    'slow_a_y_min': (2, 0x037, 25, False),
    'slow_a_hold_en': (2, 0x03b, 27, True),
    'slow_a_clear_en': (2, 0x03f, 27, True),
    'slow_a_dx_sel': (2, 0x043, 4, True),
    'slow_b_brk': (3, 0x000, 1, True),
    'slow_b_x_limit_min': (3, 0x001, 25, True),
    'slow_b_x_limit_max': (3, 0x005, 25, True),
    'slow_b_iir_z0': (3, 0x009, 38, True),
    'slow_b_iir_shift': (3, 0x00e, 5, False),
    'slow_b_iir_width': (3, 0x00f, 5, False),
    'slow_b_iir_interval': (3, 0x010, 8, False),
    'slow_b_iir_a1': (3, 0x011, 25, True),
    'slow_b_iir_a2': (3, 0x015, 25, True),
    'slow_b_iir_b0': (3, 0x019, 25, True),
    'slow_b_iir_b1': (3, 0x01d, 25, True),
    'slow_b_iir_b2': (3, 0x021, 25, True),
    'slow_b_y_limit_min': (3, 0x025, 16, True),
    'slow_b_y_limit_max': (3, 0x027, 16, True),
    'slow_b_x_clr': (3, 0x029, 1, True),
    'slow_b_x_max': (3, 0x02a, 25, False),
    'slow_b_x_min': (3, 0x02e, 25, False),
    'slow_b_y_clr': (3, 0x032, 1, True),
    'slow_b_y_max': (3, 0x033, 25, False),
    'slow_b_y_min': (3, 0x037, 25, False),
    'slow_b_hold_en': (3, 0x03b, 27, True),
    'slow_b_clear_en': (3, 0x03f, 27, True),
    'slow_b_dx_sel': (3, 0x043, 4, True),
    'slow_c_brk': (4, 0x000, 1, True),
    'slow_c_x_limit_min': (4, 0x001, 25, True),
    'slow_c_x_limit_max': (4, 0x005, 25, True),
    'slow_c_iir_z0': (4, 0x009, 38, True),
    'slow_c_iir_shift': (4, 0x00e, 5, False),
    'slow_c_iir_width': (4, 0x00f, 5, False),
    'slow_c_iir_interval': (4, 0x010, 8, False),
    'slow_c_iir_a1': (4, 0x011, 25, True),
    'slow_c_iir_a2': (4, 0x015, 25, True),
    'slow_c_iir_b0': (4, 0x019, 25, True),
    'slow_c_iir_b1': (4, 0x01d, 25, True),
    'slow_c_iir_b2': (4, 0x021, 25, True),
    'slow_c_y_limit_min': (4, 0x025, 16, True),
    'slow_c_y_limit_max': (4, 0x027, 16, True),
    'slow_c_x_clr': (4, 0x029, 1, True),
    'slow_c_x_max': (4, 0x02a, 25, False),
    'slow_c_x_min': (4, 0x02e, 25, False),
    'slow_c_y_clr': (4, 0x032, 1, True),
    'slow_c_y_max': (4, 0x033, 25, False),
    'slow_c_y_min': (4, 0x037, 25, False),
    'slow_c_hold_en': (4, 0x03b, 27, True),
    'slow_c_clear_en': (4, 0x03f, 27, True),
    'slow_c_dx_sel': (4, 0x043, 4, True),
    'slow_d_brk': (5, 0x000, 1, True),
    'slow_d_x_limit_min': (5, 0x001, 25, True),
    'slow_d_x_limit_max': (5, 0x005, 25, True),
    'slow_d_iir_z0': (5, 0x009, 38, True),
    'slow_d_iir_shift': (5, 0x00e, 5, False),
    'slow_d_iir_width': (5, 0x00f, 5, False),
    'slow_d_iir_interval': (5, 0x010, 8, False),
    'slow_d_iir_a1': (5, 0x011, 25, True),
    'slow_d_iir_a2': (5, 0x015, 25, True),
    'slow_d_iir_b0': (5, 0x019, 25, True),
    'slow_d_iir_b1': (5, 0x01d, 25, True),
    'slow_d_iir_b2': (5, 0x021, 25, True),
    'slow_d_y_limit_min': (5, 0x025, 16, True),
    'slow_d_y_limit_max': (5, 0x027, 16, True),
    'slow_d_x_clr': (5, 0x029, 1, True),
    'slow_d_x_max': (5, 0x02a, 25, False),
    'slow_d_x_min': (5, 0x02e, 25, False),
    'slow_d_y_clr': (5, 0x032, 1, True),
    'slow_d_y_max': (5, 0x033, 25, False),
    'slow_d_y_min': (5, 0x037, 25, False),
    'slow_d_hold_en': (5, 0x03b, 27, True),
    'slow_d_clear_en': (5, 0x03f, 27, True),
    'slow_d_dx_sel': (5, 0x043, 4, True),
    'xadc_temp': (29, 0x000, 12, False),
    'xadc_v': (29, 0x002, 12, False),
    'xadc_a': (29, 0x004, 12, False),
    'xadc_b': (29, 0x006, 12, False),
    'xadc_c': (29, 0x008, 12, False),
    'xadc_d': (29, 0x00a, 12, False),
}
states = ['force', 'di0', 'di1', 'di2', 'di3', 'di4', 'di5', 'di6', 'di7', 'fast_a_x_sat', 'fast_a_x_railed', 'fast_a_y_sat', 'fast_a_y_railed', 'fast_a_unlocked', 'fast_b_x_sat', 'fast_b_x_railed', 'fast_b_y_sat', 'fast_b_y_railed', 'fast_b_unlocked', 'slow_a_sat', 'slow_a_railed', 'slow_b_sat', 'slow_b_railed', 'slow_c_sat', 'slow_c_railed', 'slow_d_sat', 'slow_d_railed']
signals = ['zero', 'fast_a_x', 'fast_a_y', 'fast_b_x', 'fast_b_y', 'slow_a_x', 'slow_a_y', 'slow_b_x', 'slow_b_y', 'slow_c_x', 'slow_c_y', 'slow_d_x', 'slow_d_y', 'scopegen_dac_a', 'scopegen_dac_b', 'noise_y']
